#!/usr/bin/env python
import argparse


parser = argparse.ArgumentParser(description='Generate diff')
parser.add_argument('first_file')
parser.add_argument('second_file')
parser.add_argument('-f FORMAT', action='help',
                    help='--format FORMAT set format of output')


def main():
    parser.parse_args()


if __name__ == '__main__':
    main()
