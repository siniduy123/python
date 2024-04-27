# elements = ["a","b","c" "d","e"]
# print(len(elements)/2)
# def twosum(nums,target):
#     for num in nums:
#         for num2 in nums:
#             if num!=num2 and num+num2==target:
#              return [nums.index(num),nums.index(num2)]
# print(twosum([3,4,2],6))
word = input("type in the text to be analyzed ")
words = word.split()
word_count = len(words)   
print(f"your text is {word_count} word(s) long")         
unique_words = set()
for word in words:
    unique_words.add(word.lower())
print(unique_words)
word_frequency={}
word_lc=[word.lower()for word in words]