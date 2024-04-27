# basic structure
# try:
#     risky code
# except:
#     print("error occured")
# else:
#     print("the error did not occur")
# finally:
#     print("whether there is error or not")

try:
    file = open("thisfile.txt")
except:
    print("the file does not exist")
    
print("The program is still running")

try:
    print("String" + 3)
except:
    print("Can't concatenate string to int")
else:
    print("The code ran smoothly")
finally:
    print("The try-except block finished")
    
try:
    file = open("newFile.txt", "w")
    try:
        file.write("Writing in the file and overwriting anything in the file.")
    except:
        print("Something went wrong writing in the file")
    else:
        print("Successfully wrote in the file.")
except:
    print("Something went wrong")
else:
    print("The file is created/already exists")
finally:
    file.close()
    
try:
    x = -1
    div = x / 0
except TypeError:
    print("type error occured")
except ValueError:
    print("the variable can't hold that value")
except ZeroDivisionError:
    print("You can't divide by zero, buddy")
except:
    print("Something happened with your code")
    
# raising an exception
x = -1

if x < 0:
    # raise Exception("NegativeError")
    raise ValueError(f"x cannot have a value of {x}")
