sladkoeshkin = set(input().split())
N = int(input())
friends = []
for friend in range(N):
    friend_prefers = set(input().split())
    friends.append(friend_prefers)

only_sladkoeshkin = sladkoeshkin.difference(*friends)
print(len(only_sladkoeshkin))