
def dp_count(S, n):

    if n < 0:
        return 0

    table = [0] * (n + 1)


    table[0] = 1

    for coin_val in S:
        for j in range(coin_val, n + 1):
            table[j] += table[j - coin_val]

    return table[n]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
