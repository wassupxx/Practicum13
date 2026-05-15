from itertools import combinations

main_set = set(map(int, input().split()))
list(main_set).sort()
subsets = []
subsets.append([])
for subset_len in range(1, len(main_set) + 1):
    for combination in combinations(main_set, subset_len):
        subsets.append(list(combination))

for subset in subsets:
    print(' '.join(map(str, subset)))
