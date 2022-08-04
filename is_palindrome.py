def is_palindrome(word):
    word_lc = word.lower()
    return word_lc[0:] == word_lc[::-1]

def is_not_palindrome(word):
    return not is_palindrome(word)

my_word = 'tenet'
print(is_palindrome(my_word))
print(is_not_palindrome(my_word))