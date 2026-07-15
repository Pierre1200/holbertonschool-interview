#!/usr/bin/python3
"""Prime Game module.

Maria and Ben take turns picking a prime number from the set
{1, 2, ..., n} and removing that prime and all of its multiples
from the set. The player who cannot make a move loses.
"""


def isWinner(x, nums):
    """Determine who wins the most rounds of the Prime Game.

    Args:
        x (int): the number of rounds to play.
        nums (list): array of n values, one for each round.

    Returns:
        str: "Maria" or "Ben", whoever won the most rounds.
        None: if x or nums is invalid, or if there is a tie.
    """
    if x is None or nums is None or x < 1 or len(nums) < 1:
        return None

    n = max(nums)
    if n < 1:
        return None

    # Sieve of Eratosthenes up to n.
    sieve = [True] * (n + 1)
    sieve[0] = False
    if n >= 1:
        sieve[1] = False

    i = 2
    while i * i <= n:
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
        i += 1

    # prime_count[i] holds the number of primes in [1, i].
    prime_count = [0] * (n + 1)
    count = 0
    for i in range(2, n + 1):
        if sieve[i]:
            count += 1
        prime_count[i] = count

    maria_wins = 0
    ben_wins = 0

    for num in nums[:x]:
        if num < 1:
            ben_wins += 1
            continue
        primes_available = prime_count[num]
        # Each prime picked removes an odd-sized "chain" of choices;
        # the outcome only depends on the parity of the number of
        # primes available: odd count -> first player (Maria) wins.
        if primes_available % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    if ben_wins > maria_wins:
        return "Ben"
    return None
