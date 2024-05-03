number_of_words = int(input())
synonyms = {}

for word in range(number_of_words):
    current_word = input()
    synonym = input()
    if current_word not in synonyms.keys():
        synonyms[current_word] = []
    synonyms[current_word].append(synonym)

for word, list_of_synonym in synonyms.items():
    print(f"{word} - {', '.join(list_of_synonym)}")