number_a = int(input())
number_b = int(input())

temp_a = number_a
temp_b = number_b

number_a, number_b = number_b, number_a

print('Before:')
print(f'a = {temp_a}')
print(f'b = {temp_b}')
print('After:')
print(f'a = {number_a}')
print(f'b = {number_b}')