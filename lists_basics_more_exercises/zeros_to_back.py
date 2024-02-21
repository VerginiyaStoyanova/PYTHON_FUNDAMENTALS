string = list(map(int, input().split(',')))

for _ in range(len(string)):
    if 0 in string:
        string.remove(0)
        string.append(0)

print(string)