#!/usr/bin/env python3
import argparse
import requests


def check_url(url: str):
    """Send a GET request to the provided URL and return the status code or error."""
    try:
        response = requests.get(url, timeout=10)
        return response.status_code
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"


def main():
    parser = argparse.ArgumentParser(
        description="CLI tool to check HTTP endpoints."
    )
    parser.add_argument(
        "urls",
        nargs="+",
        help="One or more URLs to check",
    )
    args = parser.parse_args()

    for url in args.urls:
        status = check_url(url)
        print(f"{url} -> {status}")


if __name__ == "__main__":
    main()
