# Parse sites url at CLI
# import ArgumentParser
import argparse


def read_user_cli_args():
    """Handle the CLI arguments and options."""
    # prog defines program name
    parser = argparse.ArgumentParser(prog="rpchecker", description="Check availability of websites.")
    parser.add_argument(
        "-u",
        "--urls",
        metavar="URLs",
        nargs="+",
        type=str,
        default=[],
        help="Enter one or more website urls"
    )
    parser.add_argument(
        "-f",
        "--input-file",
        metavar="FILE",
        type=str,
        default="",
        help="read URLs from a file",
    )
    # Add asynchronous option
    parser.add_argument(
        "-a",
        "--asynchronous",
        action="store_true",
        help="Run connectivity checker asynchronously"
    )
    return parser.parse_args()


# Display the checked results
def display_check_result(result, url, errors=""):
    """Display results of connectivity check"""
    print(f"The status of {url} is:", end=" ")
    if result:
        print("Active! 👍")
    else:
        print(f'"Offline 👎" \n  Error: "{errors}"')