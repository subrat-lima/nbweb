import argparse

from nbweb import __VERSION__
from nbweb.app import check_is_supported, get_content, get_rss


def parse_args():
    parser = argparse.ArgumentParser(
        prog="nbweb",
        description="extracts bloat free content",
        epilog="takes in an url and returns clean content",
    )
    parser.add_argument("url", nargs="?", type=str, help="enter an url")
    parser.add_argument(
        "-f",
        "--format",
        choices=["json", "txt"],
        default="json",
        help="choose the output format. default is json",
    )

    parser.add_argument(
        "--supported", action="store_true", help="returns yes if supported else no"
    )

    parser.add_argument(
        "--rss", action="store_true", help="returns the rss information"
    )

    parser.add_argument(
        "-v", "--version", action="store_true", help="show version number"
    )

    args = parser.parse_args()
    return args


def cli() -> None:
    args = parse_args()

    if args.rss:
        content = get_rss(args.url)
    elif args.supported:
        content = check_is_supported(args.url)
    elif args.version:
        content = __VERSION__
    else:
        content = get_content(args.url, args.format)
    print(content)


if __name__ == "__main__":
    cli()
