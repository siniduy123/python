rows = int(input("how many rows?: "))
columns = int(input("how many columns?: "))
symbol = input("enter a symbol to use: ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end=" ")
        print()
      
