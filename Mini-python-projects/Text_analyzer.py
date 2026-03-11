'''
Input: Take a  Sentence

output: word count ,longest word,shortest word

concepts:  String, split, loops,comparisions

'''
import string
sent = input('Enter Sentence : ')

# 1) Split sentence into words
words = sent.split() # list formed
word_count = len(words)

# Check if the list is NOT empty before accessing index [0]
if word_count > 0:
    longest_word = words[0] # as words now  act as List because we use split(), so we assume 0th index for both as largest or smallest
    smallest_word = words[0]

    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
        if len(word) < len(smallest_word):
            smallest_word = word

    print(f'The total words are {word_count}\nThe Longest word is {longest_word}\nThe Smallest word is {smallest_word}')
else:
    print("Error: You didn't enter any words")