from datetime import datetime


def count_file_rows(file, rowskip):
    row_count = sum(1 for row in file) - rowskip
    file.seek(0)
    return row_count


def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def is_date_time(value):
    try:
        datetime.strptime(value, '%d-%m-%Y')
        return True
    except ValueError:
        return False


def is_date_time2(value):
    try:
        datetime.strptime(value, '%Y-%m-%d')
        return True
    except ValueError:
        return False
