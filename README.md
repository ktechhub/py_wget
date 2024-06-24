<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/ktechhub/doctoc)*

<!---toc start-->

- [pywgett](#pywgett)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Usage](#usage)
    - [Example usage:](#example-usage)
  - [Features](#features)
  - [GitHub](#github)
  - [License](#license)
    - [Contribution](#contribution)

<!---toc end-->

<!-- END doctoc generated TOC please keep comment here to allow auto update -->
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
Usage: pywget [OPTIONS] [URLS]...

  Download utility to fetch a file from the internet.

  Args:     urls (tuple): The URLs of the files to download.
  If multiple URLs are provided, they will be downloaded in parallel.
  If a single URL is provided, it will be downloaded serially.     output
  (str): The name of the file or directory to save the downloaded file(s) as.
  header (list): Optional HTTP headers to include in the request.     parallel
  (int): Number of parallel downloads.     verbose (bool): Enable verbose
  mode.

  Returns:     None

Options:
  -o, --output TEXT       Optional output file name or directory
  --header TEXT           Custom headers to include in the request, e.g.
                          --header 'Authorization: Bearer token', --header
                          'Content-Type: application/json', --header 'User-
                          Agent: Mozilla/5.0', etc.
  -p, --parallel INTEGER  Number of parallel downloads [default: 4]
  --verbose               Enable verbose mode to output detailed information
                          about the download process.
  --version               Show the version and exit.
  --help                  Show this message and exit.
```

### Example usage:
Single URL Download;
```sh
pywget https://www.example.com/file.zip
#or
pywget https://example.com/file.zip -o output_file.zip
```
```sh
pywget https://example.com/file.zip -o output_file.zip --header "Authorization: Bearer token" --header "User-Agent: CustomUserAgent/1.0" --verbose
```

Multiple URLS download
```sh
pywget https://example.com/file1.zip https://example.com/file2.zip -o /path/to/save -p 6
pywget https://www.ktechhub.com/assets/logo.13616b6b.png https://www.ktechhub.com/assets/logo.13616b6b.png
pywget https://example.com/file1.zip https://example.com/file2.zip -p 6
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
