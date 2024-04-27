word = input("type in the text to analyzed ")
words = word.split()
print(words)
print(f"your text is {len(words)} word(s) long")
unique_words = set()
for word in words:
    unique_words.add(word.lower())
print(unique_words)
# word_frequency = {}
# text = "there is someone someone crazyyyy is there really "
# for text in word_frequency:
#     text = t
word_frequency = {}
word_count = 0
for word in words:
    word_frequency.add(word.lower())
    if word_count in words:
        word_count = word_frequency
    else:
        word_count>0
        
        
print(word_frequency)



