#Assignment - take ur name as an input and print it in reverse direction using while loop
# ex. name = 'python'
# expected output = 'nohtyp


name = input("Enter your name: ")

i = len(name)

while i > 0:
    print(name[i-1], end="")
    i -= 1