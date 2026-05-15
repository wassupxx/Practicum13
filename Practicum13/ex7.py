from itertools import permutations

numbers = set(map(int, input().split()))
list(numbers).sort()
for perm in permutations(numbers):
    print(''.join(map(str, perm)))
