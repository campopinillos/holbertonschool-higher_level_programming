#!/usr/bin/python3
def pascal_triangle(n):
    """
    Pascal triangle
    """
    pascal_list = [[1]] if n > 0 else []
    for i in range(1, n):
        row = []
        for j in range(i + 1):
            if (j == 0 or j == i):
                row.append(1)
            else:
                row.append(pascal_list[i - 1][j - 1] + pascal_list[i - 1][j])
        pascal_list.append(row)
    return pascal_list
