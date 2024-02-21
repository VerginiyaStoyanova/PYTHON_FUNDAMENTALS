key = int(input())
number_of_lines = int(input())
message = ''

for num in range(number_of_lines):
    crypt_letter = input()
    decrypt_letter = ord(crypt_letter) + key
    message += chr(decrypt_letter)

print(message)
