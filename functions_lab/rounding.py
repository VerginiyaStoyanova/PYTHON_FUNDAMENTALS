list_numbers = list(map(float, input().split()))

# rounded_numbers = [round(number) for number in list_numbers]
rounded_numbers = list(map(lambda number: round(number), list_numbers))
print(rounded_numbers)