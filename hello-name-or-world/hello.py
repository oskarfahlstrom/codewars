"""https://www.codewars.com/kata/57e3f79c9cb119374600046b"""

def hello(name: str = ''):
    return f"Hello, {'World' if not name else name.lower().capitalize()}!"
    