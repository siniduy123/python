# tup = (1,2,"hello")
# print(tup)
# a = ("hello",)
# print(type(a))
# lst = [1,2,3]
# lst = tuple(lst)
# print(type(lst))
# print(lst[0])
# tpl1 = (0,1,2)
# tpl1 = list(tpl1)
# print(tpl1)
# tpl1.remove(0)
# # print(tpl1)
# tpl1 = tuple([i for i in range(1,11)])
# tpl1 = list(tpl1)
# print(tpl1)
# tpl1.reverse()
# print(tpl1)
# tpl1 = tuple(tpl1)
# print(tpl1)
# tpl1 = ("hello",)
# tpl2 = ("world",)
# tpl3 = tpl1+tpl2
# print(tpl3)
# tu1 = (1,3,5)
# tu2 = (2,4,6)
# tu3 = ()
# print(tu3)
# for i,j in zip(tu1,tu2):
#     tu3 +=(i,j)
# print(tu3)
# tpl12 = ("hello,")*2
# print(tpl12)
# (a,b,*c)=(1,2,3,4)
# print(a,b,tuple(c))
# import math
# vector1 = [1,2,3]
# vector2 = [4,5,6]
# summ = 0
# for i,j in zip(vector1,vector2):
#     summ += pow(i-j,2)
# distance = math.sqrt(summ)
# print(pow(distance,2))
word = input("type of text analyzed: ")
words = word.split()
print(f"your text is{len(words)} word(s) long")
unique_words =set()
for word in words:
    unique_words.add(word.lower())
print(unique_words)