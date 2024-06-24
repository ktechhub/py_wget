#!/usr/bin/env python3
"""
Download utility as an easy way to get files from the net
"""
import os
import click
from concurrent.futures import ThreadPoolExecutor
from .download import download_file, filename_from_url
from .utils import parse_headers, click_echo


@click.command()
@click.argument("urls", nargs=-1)
@click.option(
    "-o",
    "--output",
    default=None,
    help="Optional output file name or directory",
)
@click.option(
    "--header",
    multiple=True,
    help="Custom headers to include in the request, e.g. --header 'Authorization: Bearer token', --header 'Content-Type: application/json', --header 'User-Agent: Mozilla/5.0', etc.",
)
@click.option(
    "-p",
    "--parallel",
    default=4,
    help="Number of parallel downloads [default: 4]",
)
@click.option(
    "--verbose",
    is_flag=True,
    help="Enable verbose mode to output detailed information about the download process.",
)
@click.version_option(prog_name="PyWget")
def main(urls, output, header, parallel, verbose):
    """
    Download utility to fetch a file from the internet.

    Args:
        urls (tuple): The URLs of the files to download.
                      If multiple URLs are provided, they will be downloaded in parallel.
                      If a single URL is provided, it will be downloaded serially.
        output (str): The name of the file or directory to save the downloaded file(s) as.
        header (list): Optional HTTP headers to include in the request.
        parallel (int): Number of parallel downloads.
        verbose (bool): Enable verbose mode.

    Returns:
        None
    """
    headers = parse_headers(header, verbose=verbose)
    if len(urls) == 1:
        # Single URL download
        url = urls[0]
        if verbose:
            click_echo(f"Downloading {url} to {output}", color="yellow")
        filename = download_file(url, output, headers, verbose)
        click.echo(click.style(f"\nSaved under {filename}", fg="green") + f" {url}")
    else:
        # Multiple URL downloads in parallel
        if output is None:
            output = os.getcwd()
        # Multiple URL downloads in parallel
        if os.path.isfile(output):
            raise click.BadParameter("For multiple URLs, output must be a directory")

        if not os.path.exists(output):
            os.makedirs(output)

        def download_with_params(url):
            filename = os.path.join(output, filename_from_url(url))
            return download_file(url, filename, headers, verbose)

        with ThreadPoolExecutor(max_workers=parallel) as executor:
            results = list(executor.map(download_with_params, urls))

        for result, url in zip(results, urls):
            click_echo(f"Saved under {result} for {url}", color="green")


if __name__ == "__main__":
    main()
