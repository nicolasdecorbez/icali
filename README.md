# open-subject - icali

## What is this?

Icali is a Python based CLI program that convert CSV files to [ICalendars](https://en.wikipedia.org/wiki/ICalendar) files (ready to be imported in your favorite calendar). The goal was to have a first experience with Python and Poetry.

## Installation

I used [poetry](https://github.com/python-poetry/poetry) to manage all depenencies :
```console
$ git clone https://github.com/nicolasdecorbez/icali.git
$ cd icali
$ poetry install
```

## How to use it

Using the command line:
- Find a `.csv` file you want to convert (you can find examples [here](./examples)).
- (optional) Note every non-conventionnal fields (see [options](#options))
- Run icali `poetry run icali <filename> <options>`

Using the docker image:
> Work in progress

## Options

To maximize compatibility, several options are implented :

- `-h, --help` : Display help.
- `-d, --date` : Override date field (default is `"date"`)
- `-t, --title` : Override title field (default is `"title"`)
- `-o, --output` : Override output filename (default is `"calendar"`)

## Code

Code sources can be find inside [icali](icali) directory.
