import re

sentences = input()
searched_word = input()
# pattern = fr"\b{searched_word}\b"
# matches = re.findall(pattern, sentences, re.IGNORECASE)
pattern = fr"(?i)\b{searched_word}\b"
matches = re.findall(pattern, sentences)
print(len(matches))