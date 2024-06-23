# pywgett

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/ktechhub/pywgett/blob/main/LICENSE)
[![PyPI version](https://badge.fury.io/py/pywgett.svg)](https://badge.fury.io/py/pywgett)

pywgett is a command-line utility built with Python for downloading files from the internet. It provides an easy-to-use interface to fetch files using URLs, with support for custom headers, resume downloads, and more.

## Prerequisites
Before using pywgett, ensure you have the following:
- Python 3.6+
- pip (Python package installer)

## Installation
You can install pywgett using pip:

```sh
pip install pywgett
```

Alternatively, install it from the source on GitHub:

```sh
git clone https://github.com/ktechhub/pywgett.git
cd pywgett
python setup.py install
```

## Usage
Download a file from a URL:

```sh
pywget --help
Usage: pywget [OPTIONS] URL

  Download utility to fetch a file from the internet.

  Args:     url (str): The URL of the file to download.     output_file (str):
  The name of the file to save the downloaded file as.     header (list):
  Optional HTTP headers to include in the request.     verbose (bool): Enable
  verbose mode.

  Returns:     None

Options:
  -o, --output_file TEXT  Optional output file name
  --header TEXT           Custom headers to include in the request, e.g.
                          --header 'Authorization: Bearer token', --header
                          'Content-Type: application/json', --header 'User-
                          Agent: Mozilla/5.0', etc.
  --verbose               Enable verbose mode to output detailed information
                          about the download process.
  --version               Show the version and exit.
  --help                  Show this message and exit.
```

### Options:

- `-o, --output_file`: Optional output file name.
- `--header`: Custom headers to include in the request.
- `--verbose`: Enable verbose mode.

Example usage:
```sh
pywget https://www.example.com/file.zip
```

```sh
pywget https://www.example.com/file.zip --output_file my_file.zip --header "Authorization: Bearer token" --verbose
```

## Features
- Download files from URLs with ease.
- Supports custom HTTP headers for authentication and content type.
- Resume interrupted downloads automatically.
- Displays progress bar during file downloads.
- Verbose mode for detailed download process information.

## GitHub
For more details, visit the [GitHub repository](https://github.com/ktechhub/pywgett).

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Contribution
If you want to contribute, kindly see this **[contribution guide](contribution.md)**.
