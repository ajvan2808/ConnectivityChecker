import sys
import pathlib
from rpchecker.cli import read_user_cli_args, display_check_result
from rpchecker.checker import check_sites_online


def main():
    user_args = read_user_cli_args()
    urls = _get_website_urls(user_args)
    if not urls:
        print("No URL to check!", file=sys.stderr)
        sys.exit(1)
    _synchronous_check(urls)


def _get_website_urls(user_args):
    urls = user_args.urls
    if user_args.input_file:
        urls += _read_urls_from_file(user_args.input_file)
    return urls


def _read_urls_from_file(file):
    file_path = pathlib.Path(file)
    if file_path.is_file():
        with file_path.open() as urls_file:
            urls = [url.strip() for url in urls_file]
            if urls:
                return urls
            print(f"Error: empty input file, {file}", file=sys.stderr)
    else:
        print("Error: input file not found", file=sys.stderr)
    return []


def _synchronous_check(urls):
    for url in urls:
        error = ""
        try:
            result = check_sites_online(url)
        except Exception as err:
            result = False
            error = str(err)
        display_check_result(result, url, error)


if __name__ == '__main__':
    main()

