#!/usr/bin/python3
"""
Module for UTF-8 validation
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    """
    # Nombre d'octets de continuation attendus
    n_bytes = 0

    # Masques pour inspecter les bits les plus significatifs
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for num in data:
        # On ne garde que les 8 bits de poids faible (1 octet)
        byte = num & 0xFF

        if n_bytes == 0:
            # On compte le nombre de 1 consécutifs au début de l'octet de tête
            mask = 1 << 7
            while mask & byte:
                n_bytes += 1
                mask = mask >> 1

            # Caractère sur 1 octet (commence par 0)
            if n_bytes == 0:
                continue

            # UTF-8 valide uniquement pour 2, 3 ou 4 octets total
            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            # L'octet doit être un octet de continuation
            # Donc le bit de poids fort doit être 1 et le suivant doit être 0
            if not (byte & mask1 and not (byte & mask2)):
                return False

        # On a traité un octet de continuation attendu
        n_bytes -= 1

    # Si le compteur revient à 0, tous les octets requis étaient présents
    return n_bytes == 0
