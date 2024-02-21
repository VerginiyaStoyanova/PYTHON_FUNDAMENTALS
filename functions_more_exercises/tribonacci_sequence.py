def tribonacci_sequence(number):
    list_numbers = [1]
    for i in range(number - 1):
        sum_last_three = sum(list_numbers[-3:])
        list_numbers.append(sum_last_three)
    return ' '.join(str(num) for num in list_numbers)


number_as_input = int(input())
result = tribonacci_sequence(number_as_input)
print(result)