# -*- coding: utf-8 -*-
import argparse
import logging
import sys


logger_formarter = '%(levelname)s %(name)s %(asctime)s %(message)s'


def main():
    parser = argparse.ArgumentParser(
        description="build random xlxs", fromfile_prefix_chars='@'
    )
    parser.add_argument(
        '-w', '--white_rows', dest='white_rows', default=5, type=int )
    parser.add_argument(
        "--log_level", dest="log_level", default="INFO",
        help="log level 🍡",
    )
    args = parser.parse_args()
    logging.basicConfig( level=args.log_level, format=logger_formarter )

    print( args.white_rows )
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
