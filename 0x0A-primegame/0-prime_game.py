#!/usr/bin/python3
def isWinner(x, nums):
    """
    Determines the winner after x rounds.

    Args:
        x (int): Number of rounds.
        nums (list): List of n values.

    Returns:
        str: "Maria", "Ben", or None.
    """
    if not nums or x < 1:
        return None

    def sieve_of_eratosthenes(max_num):
        primes = [True] * (max_num + 1)
        primes[0] = primes[1] = False
        for i in range(2, int(max_num**0.5) + 1):
            if primes[i]:
                for j in range(i * i, max_num + 1, i):
                    primes[j] = False
        return primes

    max_num = max(nums)
    primes = sieve_of_eratosthenes(max_num)

    prime_count = [0] * (max_num + 1)
    for i in range(1, max_num + 1):
        prime_count[i] = prime_count[i - 1] + (1 if primes[i] else 0)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_count[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    return None


if __name__ == "__main__":
    print("Winner:", isWinner(5, [2, 5, 1, 4, 3]))
