# fileparse.py
#
# Exercise 3.3
import csv


def parse_csv(lines, select=None, types=None,
              has_headers=True, silence_error=False, delimiter = ',') -> list:
    """
    Parse a CSV file into a list of records with type conversion.
    """
    if not has_headers and select:
        raise RuntimeError('select argument requires column header')

    if isinstance(lines, str):
        raise RuntimeError('Dont pass a string')

    rows = csv.reader(lines, delimiter=delimiter)
    #
    # Read the file header if any
    headers = next(rows) if has_headers else []
    # If a column selector was given, find indices of the specified columns.
    # Also narrow the set of headers used for resulting dictionaries
    if select:
        indices = [headers.index(colname) for colname in select]
        headers = select
    else:
        indices = []

    records = []
    for lineno, row in enumerate(rows, 1):
        if not row:      # skipping row if no data
            continue
        # filtering the row if specific columns were selected
        if indices:
            row = [row[index] for index in indices]
        if types:
            try:
                row = [func(val) for func, val in zip(types, row)]
            except Exception as e:
                if not silence_error:
                    print(f"Row {lineno}: Couldnt convert {row} ")
                    print(f"Row {lineno}: {e}")
                continue

        # Make a dictionary  and adding to records
        if headers:
            record = dict(zip(headers, row))
        else:
            record = tuple(row)
        records.append(record)

    return records



