def string_or_not(string):
    return isinstance(string, str) and 'yes' or 'no'

word = 0
print(string_or_not(word))