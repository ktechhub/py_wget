# test_download.py

import os
import pytest
from concurrent.futures import ThreadPoolExecutor
from pywgett.download import download_file


def test_multiple_downloads():
    urls = [
        "https://www.ktechhub.com/assets/logo.13616b6b.png",
        "https://www.ktechhub.com/assets/logo.13616b6b.png",
        # Add more URLs for testing different scenarios
    ]
    output_dir = "./tests/downloads"
    os.makedirs(output_dir, exist_ok=True)

    def download_with_params(url):
        output_file = os.path.join(output_dir, os.path.basename(url))
        return download_file(url, output_file, verbose=True)

    try:
        with ThreadPoolExecutor(max_workers=4) as executor:
            results = list(executor.map(download_with_params, urls))

        for result in results:
            assert os.path.exists(result), f"File should exist after download: {result}"
    finally:
        # Clean up downloaded files
        for result in results:
            if os.path.exists(result):
                os.remove(result)
        # Clean up the output directory if it's empty
        if not os.listdir(output_dir):
            os.rmdir(output_dir)


if __name__ == "__main__":
    pytest.main()
