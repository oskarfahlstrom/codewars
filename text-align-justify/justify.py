"""https://www.codewars.com/kata/537e18b6147aa838f600001b"""

import re
import textwrap

SAMPLE = """\
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum sagittis dolor 
mauris, at elementum ligula tempor eget. In quis rhoncus nunc, at aliquet orci. Fusce 
at dolor sit amet felis suscipit tristique. Nam a imperdiet tellus. Nulla eu vestibulum 
urna. Vivamus tincidunt suscipit enim, nec ultrices nisi volutpat ac. Maecenas sit amet 
lacinia arcu, non dictum justo. Donec sed quam vel risus faucibus euismod. Suspendisse 
rhoncus rhoncus felis at fermentum. Donec lorem magna, ultricies a nunc sit amet, blandit 
fringilla nunc. In vestibulum velit ac felis rhoncus pellentesque. Mauris at tellus enim. 
Aliquam eleifend tempus dapibus. Pellentesque commodo, nisi sit amet hendrerit fringilla, 
ante odio porta lacus, ut elementum justo nulla et dolor.
"""

def justify(text: str, width: int):
    if not text: return ""
    if not len(text) > width: return text
    lines = [re.sub(r'\s+', " ", line) for line in textwrap.wrap(
        text, width=width, break_long_words=False)]
    return f"{'\n'.join(add_spaces(line, width) for line in lines[:-1])}\n{lines[-1]}"


def add_spaces(line: str, width: int):
    a, b = width-len(line), len(line.split(' '))-1
    spaces = [a // b + (1 if i < a % b else 0) for i in range(b)]
    return " ".join(w + " " * s for w, s in zip(line.split(), spaces + [0]))
   

if __name__ == '__main__':
    assert justify("aaa bbb ccc", 9) == 'aaa   bbb\nccc'
    assert justify("aa bb cc ddd eee ff gg", 9) == "aa  bb cc\nddd   eee\nff gg"
    assert justify("This is just a test.", 10) == "This    is\njust     a\ntest."
