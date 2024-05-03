while True:
    word = input()

    if word == 'end':
        break
    else:
        print(f'{word} = {word[::-1]}')