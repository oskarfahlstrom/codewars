def count(string: str) -> dict[str, int]:
    """Count occurences of each character in provided string."""
    return {char: string.count(char) for char in string}
    