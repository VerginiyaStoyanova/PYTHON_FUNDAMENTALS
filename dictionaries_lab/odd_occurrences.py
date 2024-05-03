words = input().split()
lower_list = [word.lower() for word in words]
odd_list = {}

for word in lower_list:
    if word not in odd_list:
        odd_list[word] = 0
    odd_list[word] += 1

for word, count in odd_list.items():
    if count % 2 != 0:
        print(word, end=" ")