import re

def alphanumeric(password):
    return re.match(r"^[A-Za-z0-9]+$", password) is not None