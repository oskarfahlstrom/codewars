from collections import deque


DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def string_to_matrix(s: str, n: int):
    """Convert the string representation to a 2D matrix."""
    return [list(s[i*n:(i+1)*n]) for i in range(n)]


def path_finder(maze: str):
    """Perform BFS to check if there's a path from (0, 0) to (n-1, n-1)."""
    n = len(maze.split('\n'))
    matrix = string_to_matrix(maze.replace('\n', ''), n)
    
    queue = deque([(0, 0)])  # starting point
    visited = set()
    visited.add((0, 0))
    
    while queue:
        x, y = queue.popleft()
        
        if (x, y) == (n-1, n-1):  # goal
            return True
        
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                if matrix[nx][ny] == '.':
                    queue.append((nx, ny))
                    visited.add((nx, ny))
    
    return False


if __name__ == "__main__":
    assert path_finder("\n".join([".W.", ".W.", "..."])) == True
    assert path_finder("\n".join([".W.", ".W.", "W.."])) == False
