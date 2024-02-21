
while True:
    string = input()
    if string == "End":
        break
    if string == 'SoftUni':
        continue
    new_string = ''
    for character in range(len(string)):
        new_string += string[character] * 2
    print(new_string)