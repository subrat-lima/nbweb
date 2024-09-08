import argparse

from nbweb import __VERSION__
from nbweb.app import check_is_supported, get_content


def parse_args():
    parser = argparse.ArgumentParser(
        prog="nbweb",
        description="nbweb is a simple tool to extract data from websites",
    )
    parser.add_argument("url", nargs="?", type=str, help="enter an url")
    parser.add_argument(
        "-f",
        "--format",
        choices=["json", "html", "txt"],
        default="json",
        help="choose the output format. default is json",
    )

    parser.add_argument(
        "--supported", action="store_true", help="returns yes if supported else no"
    )

    parser.add_argument(
        "-v", "--version", action="store_true", help="show version number"
    )

    args = parser.parse_args()
    return args


def cli() -> None:
    args = parse_args()

    if args.supported:
        content = check_is_supported(args.url)
    elif args.version:
        content = __VERSION__
    else:
        content = get_content(args.url, args.format)
    print(content)


if __name__ == "__main__":
    cli()
