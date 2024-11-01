def string_to_matrix(s: str) -> list[list[str]]:
    """Convert the string representation to a 2D matrix."""
    return list(map(list, s.splitlines()))

def path_finder(s: str) -> int | bool:
    """Perform search to check if there's a path from (0, 0) to (n-1, n-1)."""
    matrix, queue = string_to_matrix(s), [(0, 0, 0)]
    n = len(matrix)
    
    while queue:
        x, y, dist = queue.pop(0)  # BFS search using pop(0)
        matrix[x][y] = 'X'  # mark as visited
        
        if (x, y) == (n-1, n-1): return dist
        
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < n and 0 <= ny < n and matrix[nx][ny] == '.'): continue
            queue.append((nx, ny, dist + 1))
            matrix[nx][ny] = 'X'  # mark as visited
    
    return False

if __name__ == "__main__":
    assert path_finder("\n".join([".W.", ".W.", "..."])) == 4
    assert path_finder("\n".join([".W.", ".W.", "W.."])) == False
