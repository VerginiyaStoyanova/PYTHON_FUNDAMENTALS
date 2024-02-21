def data_type(data1, data2):
    if data1 == 'int':
        return int(data2) * 2
    elif data1 == 'real':
        return f'{(float(data2) * 1.5):.2f}'
    elif data1 == 'string':
        return f'${data2}$'


first_input = input()
second_input = input()
result = data_type(first_input, second_input)

print(result)