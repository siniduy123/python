
# recursion
# def recurring_adder(num) -> int:
#     if num > 0:
#         summation = num + recurring_adder(num - 1)
#     else:
#         return 0
#     # summation = 3 + (2 + (1 + 0))
#     return summation


# def recurring_factorial(num):
#     if num >0:
#         fac = num*recurring_factorial(num-1)
#     else:
#         return 1
#     return fac
# print(fac(3))
# def ispalindrome(s):
#     if s ==1221:
#         print(True)
#     else:
#         other
# def ispalindrome(s):
#     return str(s)[::-1]==str(s)

#     s=1221
# print(ispalindrome(121))
# @@ -0,0 +1,20 @@
products = []

def sell(product):
    pass

def restock(product, amount, unit):
    pass

def displayProducts():
    # Product name: Sugar
    # price: 80 birr/Kg
    pass

def createProduct(*, name:str, price:float, unit:str, currency:str):
    product = {"name": name, "price": price, "unit": unit, "currency": currency}
    products.append(product)
    print(products)

createProduct(name="calvin klein bag", price=400, unit="piece", currency="dollar")
# createProduct(name="Jordan Shoe", price=3000, unit="piece", currency="birr")