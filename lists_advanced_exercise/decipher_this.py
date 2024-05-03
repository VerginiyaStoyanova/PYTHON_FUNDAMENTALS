def decipher(message):
    char_number = int(''.join(char for char in message if char.isdigit()))
    letters = ''.join(char for char in message if not char.isdigit())
    if len(letters) > 1:
        letters = letters[-1] + letters[1:-1] + letters[0]
    return str(chr(char_number) + letters)


secret_message = input().split()

for current_index, current_message in enumerate(secret_message):
    secret_message[current_index] = decipher(current_message)

print(" ".join(secret_message))