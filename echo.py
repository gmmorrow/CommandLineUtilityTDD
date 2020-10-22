#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility."""

__author__ = "Gabrielle"


import sys
import argparse


def create_parser():
    parser = argparse.ArgumentParser(
        description="Perform transformation on input text."
    )
    
    parser.add_argument(
        '-u', '--upper', action='store_true',
                        help="convert text to uppercase")
    parser.add_argument(
        '-l', '--lower', action='store_true',
                        help="convert text to lowercase")
    parser.add_argument(
        '-t', '--title', action='store_true',
                        help="convert text to titlecase")
    parser.add_argument('text', help="text to be manipulated")
    return parser


def main(args):
    parser = create_parser()
    ns = parser.parse_args(args)

    if not args:
        parser.print_usage()
        sys.exit()

    text = ns.text

    if ns.upper:
        text = text.upper()
    if ns.lower:
        text = text.lower()
    if ns.title:
        text = text.title()

    print(text)
    return


if __name__ == '__main__':
    main(sys.argv[1:])
