numbers = list(map(str, input().split()))
string = input()
text = ''

for index, value in enumerate(numbers):
    digits = [int(digit) for digit in str(value)]
    sum_digits = sum(digits)
    effective_index = sum_digits % len(string)
    text += string[effective_index]
    string_list = list(string)
    if 0 <= effective_index < len(string_list):
        string_list.pop(effective_index)
    string = ''.join(string_list)

print(text)