import os
# open function
# file opening modes
    # open("file_name", "r")
# file = open("test.txt")
    # open("file_name", "a")
# file = open("text.txt", "a")
    # open("file_name", "w")
# file = open("text2.txt", "w")
    # open("file_name", "x")
# file = open("project/test2.txt", "x")

file = open("project/test.txt")

print(file.read())
file.close()

file2 = open("test.txt", "r")

print(file2.read(4))
print(file2.readline(6))
print(file2.readline())
file2.close()

file3 = open("test.txt")

for line in file3:
    for char in line:
        print(char, end="")
        
file3.close()

new_file = open("new_file.txt", "w")

new_file.write("Hello world this is a new file")


new_file = open("new_file.txt", "r")

print(new_file.read())

new_file = open("new_file.txt", "a")
new_file.write("\nHello world this is a new file")

new_file = open("new_file.txt", "r")
print(new_file.read())

# deleting files and directories
# os.remove("text2.txt")
# os.remove("project/test2.txt")
os.rmdir("project")