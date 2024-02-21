def multiplication(num_list):
    if 0 in num_list:
        return 'zero'
    else:
        negative_count = len([num for num in num_list if num < 0])
        if negative_count % 2 != 0:
            return 'negative'
        else:
            return 'positive'


first_number = int(input())
second_number = int(input())
third_number = int(input())
number_list = [first_number, second_number, third_number]

result = multiplication(number_list)
print(result)