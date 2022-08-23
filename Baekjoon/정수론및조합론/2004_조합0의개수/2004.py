def two_count(n):
    two = 0
    while n != 0:
        n = n // 2
        two += n
    return two