#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import argparse

from gendiff.generate_diff import generate_diff

def main():
    """Print difference"""
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference')
    parser.add_argument('first_file', metavar='first_file', type=str)
    parser.add_argument('second_file', metavar='second_file', type=str)
    parser.add_argument(
            '-f',
            '--format',
            action='store',
            help='set format of output',
            )
    args = parser.parse_args()
    return print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()