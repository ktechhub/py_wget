# test_verbose_mode.py

import os
import pytest
from io import StringIO
from contextlib import redirect_stdout
from pywgett.download import download_file


@pytest.mark.parametrize(
    "url",
    [
        "https://www.ktechhub.com/assets/logo.13616b6b.png",
        # Add more URLs for testing different scenarios
    ],
)
def test_verbose_output(url):
    output_file = "./tests/logo.png"
    try:
        with StringIO() as output_buffer:
            with redirect_stdout(output_buffer):
                filename = download_file(url, output_file, verbose=True)
            output = output_buffer.getvalue()
        assert os.path.exists(filename), "File should exist after download"
    finally:
        if os.path.exists(filename):
            os.remove(filename)
