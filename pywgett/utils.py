import click


def click_echo(message, color="green"):
    """
    Print a message using Click's echo function.

    Args:
        message (str): The message to print.
        color (str): The color of the message.

    Returns:
        None
    """
    click.echo(click.style(message, fg=color), color=True)


def bar_progress(current, total, width=80):
    """
    Create a progress bar.

    Args:
        current (int): The current progress.
        total (int): The total progress.
        width (int): The width of the progress bar.

    Returns:
        str: The progress bar.
    """
    if total == 0:
        return "[{}{}]".format("#" * (width - 2), " " * 0)
    avail_dots = width - 2
    shaded_dots = int(current / total * avail_dots)
    return f"[{'#' * shaded_dots}{' ' * (avail_dots - shaded_dots)}]"


def parse_headers(header_list, verbose=False):
    """
    Parse a list of headers into a dictionary.

    Args:
        header_list (list): A list of headers.
        verbose (bool): Enable verbose mode.

    Returns:
        dict: A dictionary of headers.
    """
    headers = {}
    for header in header_list:
        key, value = header.split(":", 1)
        headers[key.strip()] = value.strip()
    if verbose:
        click_echo(f"Extra Headers Supplied: {headers}", color="blue")
    return headers
