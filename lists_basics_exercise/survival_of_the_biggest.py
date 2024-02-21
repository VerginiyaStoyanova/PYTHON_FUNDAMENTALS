list_of_numbers = list(map(int, input().split()))
count_of_numbers_to_remove = int(input())

for number in range(count_of_numbers_to_remove):
    min_number = min(list_of_numbers)
    list_of_numbers.remove(min_number)

list_of_numbers = list(map(str, list_of_numbers))
print(', '.join(list_of_numbers))
