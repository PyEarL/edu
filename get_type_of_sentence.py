def get_type_of_sentence(sentence):
    last_char = sentence[-1]
    if last_char == '?':
        return 'question'
    return 'normal'

print(get_type_of_sentence('Hodor'))  # => normal
print(get_type_of_sentence('Hodor?'))