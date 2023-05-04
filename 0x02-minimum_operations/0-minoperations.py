#!/usr/bin/python3
"""This module defines the minOperations method."""


def minOperations(n):
    """This method defines the minimum operation"""

    numberOperation = 0

    while n > 1:
        factorFound = False

        if n % 2 == 0:
            numberOperation += 2
            n //= 2

        else:
            i = 3
            while i * i <= n:
                if n % i == 0:
                    factorFound = True
                    n = n // i
                    numberOperation += i
                    break
                i += 2

            if not factorFound:
                numberOperation += n
                n //= n

    return numberOperation