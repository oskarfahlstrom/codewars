def string_to_matrix(s: str):
    """Convert the string representation to a 2D matrix."""
    return list(map(list, s.splitlines()))

def path_finder(s: str):
    """Perform search to check if there's a path from (0, 0) to (n-1, n-1)."""
    matrix, queue = string_to_matrix(s), [(0, 0)]
    n = len(matrix)
    
    while queue:
        x, y = queue.pop()  # DFS search using pop()
        matrix[x][y] = 'X'  # mark as visited
        
        if (x, y) == (n-1, n-1):
            return True
        
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and (nx, ny) and matrix[nx][ny] == '.':
                queue.append((nx, ny))
    
    return False

if __name__ == "__main__":
    assert path_finder("\n".join([".W.", ".W.", "..."])) == True
    assert path_finder("\n".join([".W.", ".W.", "W.."])) == False
