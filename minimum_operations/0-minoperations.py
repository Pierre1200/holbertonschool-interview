#!/usr/bin/python3
"""
Module pour calculer le nombre minimum d'opérations
"""


def minOperations(n):
    """
    fonction pour calculer le nombre minimum d'opérations
    """
    facteur = 2
    ope = 0
    if n <= 1:
        return 0

    while n > 1:
        if n % facteur == 0:
            ope += facteur
            n = n // facteur
        else:
            facteur += 1

    return ope
