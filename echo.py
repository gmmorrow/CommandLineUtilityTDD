#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility."""

__author__ = "Gabrielle"


import sys
import argparse

def text_upper(text):
    # Coverts text to uppercase
    return text.upper()


def text_lower(text):
    # Coverts text to lowercase
    return text.lower()


def text_title(text):
    # Capitalize first letter of word
    return text.title()


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


def main(args):
    """Implementation of echo"""
    parser = create_parser()
    ns = parser.parse_args(args)
    if not ns:
        parser.print_usage()
        sys.exit(1)

    text = ns.text
    # If the namespace is -u
    #   convert text to uppercase
    # Ex: python echo.py -u 'hello'
    if ns.upper:
        text = text_upper(text)
    # If the namespace is -l
    #   convert text to uppercase
    # Ex: python echo.py -l 'hello'
    if ns.lower:
        text = text_lower(text)
    # If the namespace is -t
    #   convert text to uppercase
    # Ex: python echo.py -t 'hello'
    if ns.title:
        text = text_title(text)
    print(text)


if __name__ == '__main__':
    main(sys.argv[1:])