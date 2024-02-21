# string = input()
# lower_text = string.lower()
# target_words = ["sand", "water", "fish", "sun"]
# word_counts = sum(lower_text.count(word) for word in target_words)
#
# print(word_counts)

string = input()
lower_text = string.lower()
target_words = ["sand", "water", "fish", "sun"]
counter = 0

for word in target_words:
    counter += lower_text.count(word)

print(counter)