# x, j = 6,9
# while x>1:
#     while j>4:
#         print(j, end=" ")
#         j-=1
#         if j==4:
#             print()
#             print(x, end=" ")
#             x -=1
# l,m = 6,9
# for i in range(l,1,-1):
#     for j in range(m,4,-1):
#         print(j, end=" ")
#         if j == 4:
#             print()
# l, m = 6,9
# for i in range(l,1,-1):
#     for j in range(m,4,-1):
#         print(i,end=" ")
#         if i==1:
#             print()
# x,j = 6,9
# while x > 1:
#     while j > 4:
#         print(j, end=" ")
#         j-=1
#         if j==4:
#             print()
#             print(x,end=" ")
#             x-=1
#             if x==1:
# #              print()
# bags = ["black bag","red black","white bag"]
# items = ["bananas","orange","grapes"]
# cart = {}
# # cart = {"black bag":["grapes,orange"], "red bag":["orange"], "white bag":["bananas,grapes"] }
# print(cart)
for bag in bags:
 rand = random.randint(1,5)
for i in range(rand):
    cart[bag] = items[:1]
    cart[bag] = items
    cart[bag] = [item for item in items]
    bag_items = cart.get(bag,[])
    for item in items:
        bag_items.append(item)
        print(f"{cart = }")
        
