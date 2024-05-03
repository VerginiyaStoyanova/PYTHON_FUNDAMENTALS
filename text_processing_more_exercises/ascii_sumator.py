start_char = ord(input())
end_char = ord(input())
string = input()
sum_of_chars = 0

for char in string:
    if start_char < ord(char) < end_char:
        sum_of_chars += ord(char)

print(sum_of_chars)