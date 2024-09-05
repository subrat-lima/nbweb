#!/usr/bin/env python3

import hashlib
import sys

from nbweb.extractor import get_extractor_by_name


def match_value(a, b):
    if isinstance(a, str):
        if a.startswith("md5:"):
            b = "md5:" + hashlib.md5(b.encode("utf-8")).hexdigest()
        if a == b:
            return True
    print(f"error matching {a} == {b}")
    return False


def run_test(extractor, test):
    info_dict = extractor._extract(test["url"])
    for key, value in test["info_dict"].items():
        if match_value(value, info_dict[key]):
            continue
        sys.exit(1)


def run_tests():
    if len(sys.argv) < 2:
        print("Error: arguments missing")
        print_usage()
        sys.exit(1)
    extractor = get_extractor_by_name(sys.argv[1])
    tests = extractor._TESTS
    for test in tests:
        run_test(extractor, test)
    print("test successful")


def print_usage():
    print("\nUsage:")
    print(f"{sys.argv[0]} <Extractor>\n")
    print("Example:")
    print(f"{sys.argv[0]} OTVIE\n\n")


if __name__ == "__main__":
    run_tests()
