import re

def strip_comments(s: str, markers: list[str]) -> str:
    pattern = f"[{re.escape(''.join(markers) if markers else '*')}].*"
    return '\n'.join(re.sub(pattern, '', line).rstrip() for line in s.splitlines())
    

if __name__ == '__main__':
    assert strip_comments('a #b\nc\nd $e f g', ['#', '$']) == 'a\nc\nd'
    assert strip_comments(' a #b\nc\nd $e f g', ['#', '$']) == ' a\nc\nd'