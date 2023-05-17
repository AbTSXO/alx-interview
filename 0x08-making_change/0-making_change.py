#!/usr/bin/python3
'''Given a pile of coins of different values,
    determine the fewest number of coins needed to meet
    a given amount total.
'''
import sys


def makeChange(coins, total):
    '''
    Return: fewest number of coins needed to meet total
    If total is 0 or less, return 0
    If total cannot be met by any number of coins you have, return -1
    '''
    if total <= 0:
        return 0
    tb = [sys.maxsize for i in range(total + 1)]
    tb[0] = 0
    m = len(coins)
    for i in range(1, total + 1):
        for j in range(m):
            if coins[j] <= i:
                subres = tb[i - coins[j]]
                if subres != sys.maxsize and subres + 1 < tb[i]:
                    tb[i] = subres + 1

    if tb[[total] == sys.maxsize:
        return -1
    return tb[total]
