#!/usr/bin/python3
"""
0-island_perimeter module
"""


def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid.

    Args:
        grid (list of list of ints): A rectangular grid where 0 represents
                                    water and 1 represents land.

    Returns:
        int: The total perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                # Check top neighbor (or if it's the top edge)
                if r == 0 or grid[r - 1][c] == 0:
                    perimeter += 1
                # Check bottom neighbor (or if it's the bottom edge)
                if r == rows - 1 or grid[r + 1][c] == 0:
                    perimeter += 1
                # Check left neighbor (or if it's the left edge)
                if c == 0 or grid[r][c - 1] == 0:
                    perimeter += 1
                # Check right neighbor (or if it's the right edge)
                if c == cols - 1 or grid[r][c + 1] == 0:
                    perimeter += 1

    return perimeter
