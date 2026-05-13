#!/usr/bin/python3
"""
Module pour générer le triangle de Pascal
"""


def pascal_triangle(n):
    """
    Renvoie une liste de listes d'entiers représentant le triangle de Pascal.
    """
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = [1]
        if i > 0:
            prev_row = triangle[-1]
            for j in range(len(prev_row) - 1):
                somme = prev_row[j] + prev_row[j + 1]
                row.append(somme)
            row.append(1)
        triangle.append(row)

    return triangle
