#!/usr/bin/env python3
"""
Download utility as an easy way to get files from the net
"""
import click

from .download import download_file
from .utils import parse_headers


@click.command()
@click.argument("url")
@click.option(
    "-o",
    "--output_file",
    default=None,
    help="Optional output file name",
)
@click.option(
    "--header",
    multiple=True,
    help="Custom headers to include in the request, e.g. --header 'Authorization: Bearer token', --header 'Content-Type: application/json', --header 'User-Agent: Mozilla/5.0', etc.",
)
@click.option(
    "--verbose",
    is_flag=True,
    help="Enable verbose mode to output detailed information about the download process.",
)
@click.version_option(prog_name="PyWget")
def main(url, output_file, header, verbose):
    """
    Download utility to fetch a file from the internet.

    Args:
        url (str): The URL of the file to download.
        output_file (str): The name of the file to save the downloaded file as.
        header (list): Optional HTTP headers to include in the request.
        verbose (bool): Enable verbose mode.

    Returns:
        None
    """
    if verbose:
        click.echo(click.style(f"Downloading {url} to {output_file}", fg="yellow"))
    headers = parse_headers(header, verbose=verbose)
    filename = download_file(url, output_file, headers, verbose=verbose)
    click.echo(click.style(f"\nSaved  {url} as {filename}", fg="green"))


if __name__ == "__main__":
    main()
