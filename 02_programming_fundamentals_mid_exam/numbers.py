numbers = list(map(int, input().split()))
average_value = sum(numbers) / len(numbers)
new_list = []
count = 0

for number in numbers:
    if number > average_value:
        new_list.append(number)
        count += 1

if new_list:
    descending_list = sorted(new_list, reverse=True)[:5]
    print(' '.join(str(number) for number in descending_list))
else:
    print("No")