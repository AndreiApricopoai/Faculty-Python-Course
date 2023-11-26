def is_not_empty(value):
    return value != ''


def is_type(value, expected_type):
    try:
        expected_type(value)
        return True
    except ValueError:
        return False
