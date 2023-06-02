#!/usr/bin/python3

""" Function to find perimiter of an island """


def island_perimeter(grid):
    """
    Input: List of Lists
    Returns: Perimeter of the island
    """
    c = 0
    r = len(grid)
    co = len(grid[0]) if r else 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):

            idx = [(i - 1, j), (i, j - 1), (i, j + 1), (i + 1, j)]
            check = [1 if k[0] in range(r) and k[1] in range(co) else 0
                     for k in idx]

            if grid[i][j]:
                c += sum([1 if not r or not grid[k[0]][k[1]] else 0
                              for r, k in zip(check, idx)])

    return (c)
