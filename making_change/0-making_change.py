#!/usr/bin/python3
"""
0-making_change module
"""
import math


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given amount total.

    Parameters:
    coins (list): A list of the values of the coins in your possession.
    total (int): The total amount to meet.

    Returns:
    int: Fewest number of coins needed to meet total.
         0 if total is 0 or less.
         -1 if total cannot be met.
    """
    if total <= 0:
        return 0

    if not coins:
        return -1

    # Remove duplicates and sort in descending order to favor larger coins first
    coins = sorted(list(set(coins)), reverse=True)

    # Optimization 1: Quick GCD check. If total isn't divisible by the
    # greatest common divisor of all available coins, it's impossible.
    g = coins[0]
    for c in coins[1:]:
        g = math.gcd(g, c)
        if g == 1:
            break
    if total % g != 0:
        return -1

    res = float('inf')
    n = len(coins)

    def dfs(index, count, remains):
        nonlocal res
        if remains == 0:
            res = min(res, count)
            return

        coin = coins[index]

        # Optimization 2: If we are at the last available coin denomination,
        # check if it can cleanly divide the remaining balance without looping.
        if index == n - 1:
            if remains % coin == 0:
                res = min(res, count + remains // coin)
            return

        # Loop from using the maximum possible number of this coin down to 0
        for k in range(remains // coin, -1, -1):
            # Optimization 3 (Pruning): Calculate the absolute best-case lower
            # bound for the remaining balance using the next largest coin.
            # If this bound cannot beat our current best result (`res`), break.
            next_coin = coins[index + 1]
            lower_bound = count + k + (remains - k * coin + next_coin - 1) // next_coin
            if lower_bound >= res:
                break
            
            dfs(index + 1, count + k, remains - k * coin)

    dfs(0, 0, total)
    return res if res != float('inf') else -1