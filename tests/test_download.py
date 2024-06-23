# test_download.py

import os
import pytest
from pywgett.download import download_file


@pytest.mark.parametrize(
    "url",
    [
        "https://www.ktechhub.com/assets/logo.13616b6b.png",
        # Add more URLs for testing different scenarios
    ],
)
def test_download_file(url):
    output_file = "./tests/logo.png"
    try:
        filename = download_file(url, output_file)
        assert os.path.exists(filename), "File should exist after download"
    finally:
        if os.path.exists(filename):
            os.remove(filename)
