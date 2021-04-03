""" Read command line args and
    return all parameters to use """

import argparse
from dataclasses import dataclass


@dataclass
class Parameters:
    """ Create a list of parameters for the csv_reader function """
    filename: ""
    date: ""
    title: ""
    output: ""


def generate_params(filename, date, title, output):
    """ Format function arguments into a Parameters object """
    params = Parameters(filename, date, title, output)
    return params


def get_args():
    """ Define all accepted arguments and return a Parameters object """
    parser = argparse.ArgumentParser()

    parser.add_argument("file",
                        type=argparse.FileType('r'),
                        help=".csv file to read")
    parser.add_argument("-d", "--date",
                        help="Override date column name",
                        default="date")
    parser.add_argument("-t", "--title",
                        help="Override title column name",
                        default="title")
    parser.add_argument("-o", "--output",
                        help="Override output filename",
                        default="calendar")

    args = parser.parse_args()
    return generate_params(args.file.name, args.date, args.title, args.output)
