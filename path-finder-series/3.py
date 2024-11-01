import heapq

def string_to_matrix(s: str) -> list[list[int]]:
    """Convert the string representation to a 2D matrix of integers."""
    return [list(map(int, line)) for line in s.splitlines()]

def path_finder(s: str) -> int:
    """Perform search to check if there's a path from (0, 0) to (n-1, n-1)."""
    matrix = string_to_matrix(s)
    n = len(matrix)

    queue = [(0, 0, 0)]  # cost, x, y
    costs = {(0, 0): 0}  # keep track of min costs for each visited tile
    
    while queue:
        c, x, y = heapq.heappop(queue)  # always process the cell with the lowest current cost
        
        if (x, y) == (n-1, n-1): return c      
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy

            if not (0 <= nx < n and 0 <= ny < n): continue
            mc = abs(matrix[x][y] - matrix[nx][ny])
            nc = c + mc
            
            if (nx, ny) in costs and not nc < costs[(nx, ny)]: continue
            costs[(nx, ny)] = nc
            heapq.heappush(queue, (nc, nx, ny))

if __name__ == "__main__":
    assert path_finder("\n".join(["000", "000", "000"])) == 0
    assert path_finder("\n".join(["010", "010", "010"])) == 2
    assert path_finder("\n".join(["010", "101", "010"])) == 4
    assert path_finder("\n".join(["110", "010", "011"])) == 0
