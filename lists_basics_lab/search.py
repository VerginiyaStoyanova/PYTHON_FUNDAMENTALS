n = int(input())
word = input()
strings_list =[]
list_word = []

for _ in range(n):
    string = input()
    strings_list.append(string)
    if word in string:
        list_word.append(string)

print(strings_list)
print(list_word)