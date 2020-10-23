#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility."""

__author__ = "Gabrielle"


import sys
import argparse


def create_parser():
    """Returns an instance of argparse.ArgumentParser"""
    paser = argparse.ArgumentParser(
        description='Perform transformation on input text.')
    paser.add_argument(
        '-u', '--upper', help='convert text to uppercase', action='store_true')

    paser.add_argument(
        '-l', '--lower', help='convert text to lowercase', action='store_true')

    paser.add_argument(
        '-t', '--title', help='convert text to titlecase', action='store_true')

    paser.add_argument('text', help='text to be manipulated')
    return paser


def text_uppercase(text):
    return text.upper()


def text_lowercase(text):
    return text.lower()


def text_title(text):
    return text.title()


def main(args):
    """Implementation of echo"""
    parser = create_parser()
    ns = parser.parse_args(args)
    if not ns:
        parser.print_usage()
        sys.exit(1)

    text = ns.text
    if ns.upper:
        text = text_uppercase(text)

    if ns.lower:
        text = text_lowercase(text)

    if ns.title:
        text = text_title(text)
    print(text)


if __name__ == '__main__':
    main(sys.argv[1:])
