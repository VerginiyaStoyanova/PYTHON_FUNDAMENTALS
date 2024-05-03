def count_even_numbers():
    numbers = list(map(int, input().split(", ")))
    indexes = [index for index, number in enumerate(numbers) if number % 2 == 0]
    return indexes


result = count_even_numbers()
print(result)