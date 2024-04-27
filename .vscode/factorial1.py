products = []
def sell(product):
    pass
def restock(product,amount,unit):
    pass
def restock(product,amount):
    pass
def displayproduct():
    pass
for product in products:
            print(f"Product name: {product["name"]}\nPrice: {product["price"]} {product["currency"]}/{product["unit"]}")
            print()
def createproduct(*,name:str,price:float,currency:str,unit:str):
          product ={"name":name, "price":price,"currency":currency,"unit":unit}
          products.append(product)
          print(products)
createproduct(name = "louis voitun jacket",price = 900, currency = "dollar", unit = "piece")
createproduct(name="rose flower",price=500,currency="birr",unit="piece")
displayproduct()
        
    
    
