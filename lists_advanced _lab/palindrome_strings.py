def is_it_a_palindrome():
    words = input().split()
    palindrome = input()
    filtered_words = list(filter(lambda word: word == word[::-1], words))
    print(filtered_words)
    count = filtered_words.count(palindrome)
    return count


result = is_it_a_palindrome()
print(f"Found palindrome {result} times")