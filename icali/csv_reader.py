import csv
from . import read_input
import sys
from ics import Calendar, Event
from dataclasses import dataclass

@dataclass
class Positions:
    title: ""
    date: ""
    description: ""

def generate_pos(title, date, description):
    params = Positions(title, date, description)
    return params

# ---- #

# Determine the position of each field in CSV file
def get_position(input, toFind):
    position = 0;
    for field in input:
        if field == toFind:
            return position
        else:
            position += 1
    sys.exit(f"Error : field '{toFind}' doesn't exist. Exiting the program...")

# Add .ics extension to filename if missing
def verify_filename(filename):
    type=".ics"
    if filename.endswith(type):
        return filename;
    else :
        toret=filename+type
        return toret

def export_calendar(c, filename):
    filename = verify_filename(filename)
    try:
        with open(filename, 'w') as f:
            f.writelines(c)
        print(f"File {filename} created in current directory.")
    except Exception as e:
        sys.exit(e)


def create_calendar():
    c = Calendar()
    parameters = read_input.get_args()
    with open(parameters.filename, newline='') as csvfile:
        csv_opener = csv.reader(csvfile, delimiter=',')
        for index, row in enumerate(csv_opener):
            if index == 0:
                positions = generate_pos(get_position(row, parameters.title), get_position(row, parameters.date), get_position(row, "description"))
            else:
                e = Event()
                e.name = row[positions.title]
                e.begin = row[positions.date]
                e.description = row[positions.description]
                c.events.add(e)
        try:
            print(f"Created {index} events.")
            export_calendar(c, parameters.output)
        except Exception as e:
            sys.exit(e)
