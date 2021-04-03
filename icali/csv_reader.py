""" Read CSV files and create ICS Calendar and Events """

import sys
from csv import DictReader
from ics import Calendar, Event as CalendarEvent
from icali import read_input


def verify_filename(filename):
    """ Add .ics extension to filename if missing """
    extension = ".ics"
    if not filename.endswith(extension):
        filename = filename + extension
    return filename


def export_calendar(calendar, filename):
    """ Export the Calendar into .ics file """
    filename = verify_filename(filename)
    try:
        with open(filename, 'w') as file:
            file.writelines(calendar)
        print(f"File {filename} created in current directory.")
    except OSError:
        print(f"Could not open/read {filename}")
        sys.exit()


def create_calendar():
    """ Read .csv file and create Events and Calendar """
    calendar = Calendar()
    index = None
    parameters = read_input.get_args()
    with open(parameters.filename, newline='') as csvfile:
        csv_opener = DictReader(csvfile, delimiter=',')
        for index, row in enumerate(csv_opener):
            event = CalendarEvent()
            event.name = row[parameters.title]
            event.begin = row[parameters.date]
            event.description = row["description"]
            calendar.events.add(event)
        print(f"Created {index + 1} events.")
        export_calendar(calendar, parameters.output)
