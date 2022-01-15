#!/usr/bin/python3
#  -*- coding: utf-8 -*-

import os
import sys
import logging
import re
import csv


def get_csv_files(cwd=None, pattern=''):
    if cwd is None:
        cwd = os.getcwd()
    matched_files = []
    pattern = re.compile(pattern, re.IGNORECASE)
    for root, _, files in os.walk(cwd, topdown=True):
        for file in files:
            if 'decsep' in file:
                continue
            if pattern.match(file):
                matched_files.append(os.path.join(root, file))
    return matched_files


def convert_file(file):
    rows = []
    with open(file, newline='') as csvfile:
        spamreader = csv.reader(
            csvfile,
            # dialect='excel',
            lineterminator='\r\n',
            delimiter=',',
            quotechar='"',
        )
        for row in spamreader:
            row = [to_float(v) for v in row]
            rows.append(row)

    new_filename = '{}_decsep.csv'.format(file.strip('.csv'))
    logging.info(f'New file created: {new_filename}')
    with open(new_filename, 'w', newline='') as csvfile:
        spamwriter = csv.writer(
            csvfile,
            delimiter=';',
            quoting=csv.QUOTE_MINIMAL,
            # escapechar='"',
        )
        spamwriter.writerows(rows)


def to_float(str_):
    number = str_.replace(',', '.')
    try:
        return float(number)
    except ValueError:
        return str_


if __name__ == '__main__':
    logging.basicConfig(
        filename=os.path.join(os.getcwd(), 'conversion.log'), 
        # encoding='utf-8', 
        level=logging.INFO
        )

    try:
        filename_pattern = sys.argv[1]
    except IndexError:
        filename_pattern = 'Specimen_RawData_1.csv'
    csv_files = get_csv_files(pattern=filename_pattern)
    for file in csv_files:
        convert_file(file)
    logging.info('# ----END OF RUN-------------')
