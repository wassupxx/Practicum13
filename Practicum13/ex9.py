from itertools import combinations

numbers = sorted(set(map(int, input().split())))
N = len(numbers)
K = int(input())
subsets = []

if K > N:
    K = int(input())

for combination in combinations(numbers, K):
    subsets.append(list(combination))

for subset in subsets:
    print(' '.join(map(str, subset)))
