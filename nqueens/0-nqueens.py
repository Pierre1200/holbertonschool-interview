#!/usr/bin/python3
"""
Module pour résoudre le problème des N-Reines (N-Queens Puzzle).
Utilise un algorithme de backtracking pour trouver toutes les solutions.
"""
import sys


def print_usage_and_exit():
    """Imprime le message d'usage standard et quitte avec le statut 1."""
    print("Usage: nqueens N")
    sys.exit(1)


def validate_input():
    """
    Valide les arguments de la ligne de commande.
    Retourne la valeur de N convertie en entier si elle est valide.
    """
    # 1. Vérifie si le nombre d'arguments est correct
    if len(sys.argv) != 2:
        print_usage_and_exit()

    # 2. Vérifie si l'argument est bien un entier
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # 3. Vérifie si l'entier est supérieur ou égal à 4
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    return n


def is_safe(board, row, col):
    """
    Détermine si on peut placer une reine à la position (row, col).
    'board'une liste où l'index représente la ligne et la valeur la colonne.
    """
    for r in range(row):
        # Vérifie si une reine existe déjà sur la même colonne
        if board[r] == col:
            return False
        # Vérifie si une reine existe sur la même diagonale
        # [INDICE : Utilise la formule de la valeur absolue abs()]
        if abs(board[r] - col) == abs(r - row):
            return False
    return True


def solve_nqueens(n, row, board):
    """
    Fonction récursive de backtracking pour placer les reines
    ligne par ligne (row).
    """
    # Cas de base : si toutes les reines sont placées (row == n)
    if row == n:
        # Formate et imprime la solution trouvée au format demandé
        # Exemple attendu : [[0, c0], [1, c1], ...]
        solution = [[r, board[r]] for r in range(n)]
        print(solution)
        return

    # Explore toutes les colonnes possibles pour la ligne 'row'
    for col in range(n):
        if is_safe(board, row, col):
            # Place la reine temporairement
            board[row] = col

            # Passe à la ligne suivante (appel récursif)
            solve_nqueens(n, row + 1, board)

            # Backtrack : On n'a pas besoin de nettoyer explicitement
            # car la valeur sera écrasée au prochain tour de boucle.


def main():
    """Point d'entrée principal du programme."""
    n = validate_input()

    # 'board' stocke les positions des reines : index = ligne, valeur = colonne
    # On l'initialise avec des zéros (ou n'importe quelle valeur)
    board = [0] * n
    # Lance la résolution à partir de la ligne 0
    solve_nqueens(n, 0, board)


if __name__ == "__main__":
    main()
