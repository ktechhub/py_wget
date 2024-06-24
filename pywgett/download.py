#!/usr/bin/env python3
"""
Download utility as an easy way to get files from the net
"""
import sys
import os
import shutil
import tempfile
import requests
from urllib.parse import urlparse

from .utils import bar_progress, click_echo


def filename_from_url(url):
    """
    Get the filename from a URL.

    Args:
        url (str): The URL to get the filename from.

    Returns:
        str: The name of the file the downloaded file was saved as.
    """
    return os.path.basename(urlparse(url).path) or "download.wget"


def download_file(url, out=None, headers={}, verbose=False, quiet=False):
    """
    Download a file from the internet.

    Args:
        url (str): The URL of the file to download.
        out (str): The name of the file to save the downloaded file as.
        headers (dict): Optional HTTP headers to include in the request.
        quiet (bool): Suppress output and run silently except for errors or essential messages.

    Returns:
        str: The name of the file the downloaded file was saved as.
    """
    out = out or filename_from_url(url)
    tmpfile = tempfile.mktemp(dir=".", prefix=out, suffix=".tmp")

    with requests.get(url, headers=headers, stream=True) as r:
        r.raise_for_status()
        total_size = int(r.headers.get("content-length", 0))
        current_size = 0

        with open(tmpfile, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
                    current_size += len(chunk)
                    progress_bar = bar_progress(current_size, total_size)
                    if verbose:
                        click_echo(
                            f"\r{progress_bar} {current_size}/{total_size if total_size else 'unknown'} bytes for {url}",
                            color="blue",
                            quiet=quiet,
                        )
                    sys.stdout.flush()

    sys.stdout.write("\n")

    if os.path.exists(out):
        base, ext = os.path.splitext(out)
        count = 1
        while os.path.exists(out):
            out = f"{base} ({count}){ext}"
            count += 1

    shutil.move(tmpfile, out)
    if verbose:
        click_echo(f"Downloaded {url} to {out}", color="green", quiet=quiet)
    return out
