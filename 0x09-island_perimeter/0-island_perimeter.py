#!/usr/bin/python3
"""
Calculate the perimeter of an island in a grid.
"""


def island_perimeter(grid):
    """
    Returns the perimeter of the island in the grid.

    Args:
        grid (list of list of ints): Grid where 1 is land, 0 is water.

    Returns:
        int: The perimeter of the island.
    """
    rows, cols = len(grid), len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4
                if i > 0 and grid[i - 1][j] == 1:  # Top neighbor
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:  # Left neighbor
                    perimeter -= 2

    return perimeter
