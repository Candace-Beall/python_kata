word = 'crow'

reverse_word = None
reverse_word = 'worc'

assert 'worc' == reverse_word

word = 'blue dog'
reverse_word = ''

for character in word:
    reverse_word = character + reverse_word

assert 'god eulb' == reverse_word

word_list = ['f', 'o', 'u', 'r']

word_length = len(word_list)
half_word_length = (word_length / 2) - 1

for left_index, _ in enumerate(word_list):
    right_index = word_length - (left_index + 1)

    left_character = word_list[left_index]
    right_character = word_list[right_index]

    word_list[left_index] = right_character
    word_list[right_index] = left_character

    if left_index >= half_word_length:
        break

assert 'ruof' == ''.join(word_list)
