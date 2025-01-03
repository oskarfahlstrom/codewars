"""https://www.codewars.com/kata/520446778469526ec0000001"""


def same_structure_as(original, other):
    if isinstance(original, list) and isinstance(other, list):
        if len(original) != len(other): return False
        return all(same_structure_as(o1, o2) for o1, o2 in zip(original, other))
    return not isinstance(original, list) and not isinstance(other, list)


if __name__ == '__main__':
    assert same_structure_as([1,[1,1]],[2,[2,2]]) == True
    assert same_structure_as([1,[1,1]],[[2,2],2]) == False
    assert same_structure_as([1,'[',']'], ['[',']',1]) == True
