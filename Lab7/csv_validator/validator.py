from .reader import read_csv
from .rules import is_not_empty, is_type


def validate_csv(file_path, type_rules):
    rows = read_csv(file_path)
    valid_rows = []

    for row in rows:
        if not all(is_not_empty(value) for value in row.values()):
            continue

        if not all(is_type(row[column], data_type) for column, data_type in type_rules.items()):
            continue

        valid_rows.append(row)

    return valid_rows
