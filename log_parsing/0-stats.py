#!/usr/bin/python3
import sys

taille_totale = 0
compteur = 0
status_counts = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0,
}


def print_stats():
    print("File size: {}".format(taille_totale))
    for code, count in sorted(status_counts.items()):
        if count > 0:
            print("{}: {}".format(code, count))


if __name__ == "__main__":
    try:
        for line in sys.stdin:
            tokens = line.split()
            if len(tokens) < 2:
                continue
            statut_potentiel = tokens[-2]
            taille_potentielle = tokens[-1]
            try:
                taille = int(taille_potentielle)
                statut = int(statut_potentiel)
            except ValueError:
                continue

            taille_totale += taille
            if statut in status_counts:
                status_counts[statut] += 1
            compteur += 1
            if compteur == 10:
                print_stats()
                compteur = 0

    except KeyboardInterrupt:
        print_stats()
        raise
