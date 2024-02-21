number_of_lines = int(input())
string = ''
is_balanced = True

for _ in range(number_of_lines):
    character = input()
    if character == ')':
        if '(' not in string:
            is_balanced = False
            break
    elif character == '(':
        if '(' in string and ')' not in string:
            is_balanced = False
            break
    string += character

if is_balanced:
    print('BALANCED')
else:
    print('UNBALANCED')