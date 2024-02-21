string = input()
capital_count = []

for index, char in enumerate(string):
    if char.isupper():
        capital_count.append(index)

print(capital_count)