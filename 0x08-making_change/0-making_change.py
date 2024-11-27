#!/usr/bin/python3
def makeChange(coins, total):
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        if total <= 0:
            break
        count += total // coin
        total %= coin
    return count if total == 0 else -1
