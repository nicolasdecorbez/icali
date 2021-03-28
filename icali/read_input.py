import argparse
from dataclasses import dataclass

@dataclass
class Parameters:
    filename: ""
    date: ""
    title: ""
    output: ""

def generate_params(filename, date, title, output):
    params = Parameters(filename, date, title, output)
    return params

def get_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("file", type=argparse.FileType('r'), help=".csv file to read")

    parser.add_argument("-d", "--date", help="Override date column name", default="date")
    parser.add_argument("-t", "--title", help="Override title column name", default="title")
    parser.add_argument("-o", "--output", help="Override default output filename", default="calendar")

    args = parser.parse_args()
    return generate_params(args.file.name, args.date, args.title, args.output)
