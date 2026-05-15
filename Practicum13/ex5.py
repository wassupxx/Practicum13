def sieve_of_eratosthenes(n):
    """
    Находит все простые числа, меньшие n, используя алгоритм решета Эратосфена.
    """
    if n <= 2:
        return set()

    numbers = set(range(2, n))

    for i in range(2, int(n ** 0.5) + 1):
        if i in numbers:
            multiples = set(range(i * i, n, i))
            numbers -= multiples

    return numbers
