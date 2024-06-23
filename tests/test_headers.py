import os
import pytest
from pywgett.download import download_file


@pytest.mark.parametrize(
    "url, headers",
    [
        (
            "https://www.ktechhub.com/assets/logo.13616b6b.png",
            {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
            },
        ),
        # Add more URLs and headers for testing different scenarios
    ],
)
def test_download_with_headers(url, headers):
    output_file = "./tests/logo.png"
    try:
        filename = download_file(url, output_file, headers=headers)
        assert os.path.exists(filename), "File should exist after download"
    finally:
        if os.path.exists(filename):
            os.remove(filename)
