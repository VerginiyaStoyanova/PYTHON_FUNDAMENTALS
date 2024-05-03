morse_string = input().split()

morse_letters = {'A': '.-', 'B': '-...',
                 'C': '-.-.', 'D': '-..', 'E': '.',
                 'F': '..-.', 'G': '--.', 'H': '....',
                 'I': '..', 'J': '.---', 'K': '-.-',
                 'L': '.-..', 'M': '--', 'N': '-.',
                 'O': '---', 'P': '.--.', 'Q': '--.-',
                 'R': '.-.', 'S': '...', 'T': '-',
                 'U': '..-', 'V': '...-', 'W': '.--',
                 'X': '-..-', 'Y': '-.--', 'Z': '--..',
                 }
new_string = ''

for char in morse_string:
    letter = ''
    if char != '|':
        letter = next(key for key, value in morse_letters.items() if value == char)
        new_string += letter
    else:
        new_string += char

print(new_string.replace('|', ' '))