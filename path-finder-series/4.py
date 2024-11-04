import re

def i_am_here(path: str):
    p = re.sub(r'([a-zA-Z])(\d*)', lambda x: x[1] * int(x[2] or 1), path)
    return [(p.count('l') - p.count('R')), (p.count('r') - p.count('L'))]


if __name__ == "__main__":
    assert i_am_here('') == [0, 0]
    assert i_am_here('RLrl') == [0, 0]
    assert i_am_here('r5L2l4') == [4, 3]
    assert i_am_here('r5L2l4') == [0, 0]
    assert i_am_here('10r5r0') == [-10, 5]
    assert i_am_here('10r5r0') == [0, 0]
    