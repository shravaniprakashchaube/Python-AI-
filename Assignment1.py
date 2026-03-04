#Assignment: Remaining methods of a string
''' capitalize(): Converts the first character to uppercase and the rest to lowercase.
    lower(): Converts all characters in the string to lowercase.
    upper(): Converts all characters in the string to uppercase
    title(): Converts the first character of each word to uppercase.
    swapcase(): Swaps cases, making lowercase letters uppercase and vice versa'''

txt = "hello"

x = txt.capitalize()

print (x)

txt = "Hello "

x = txt.lower()

print(x)

txt = "Hello "

x = txt.upper()

print(x)

txt = "hello"

x = txt.title()

print(x)

txt = "Hello "

x = txt.swapcase()

print(x)

'''Searching and Finding Methods like count(), find(), and index() 
are used to locate substrings within a string.'''

txt = "I love apples, apple are my favorite fruit"

x = txt.count("apple")

print(x)

txt = "Hello, welcome to my world."

x = txt.index("welcome")

print(x)

#The endswith() method returns True if the string ends with the specified value, otherwise False.

txt = "Hello, welcome to my world."

x = txt.endswith(".")

print(x)

txt = "Hello, welcome to my world."

x = txt.startswith("Hello")

print(x)

'''Splitting and Joining The split() method divides a string into a list based on a separator. Conversely, join() combines items from an iterable into a string, using the original string as the separator.'''

txt = "welcome to the class"
x = txt.split()
print(x)

myTuple = ("abc", "std", "pqr")

x = '#'.join(myTuple)

print(x)

#Formatting and Trimming Strings can be trimmed using strip(), lstrip(), and rstrip() to remove leading/trailing whitespace or specified characters.

txt = " mango "

x = txt.strip()

print("of all fruits", x, "is my favorite")

txt = "banana"

x = txt.lstrip()

print("of all fruits", x, "is my favorite")

txt = "banana"

x = txt.rstrip()

print("of all fruits", x, "is my favorite")

txt = "I like bananas"

x = txt.replace("bananas", "apples")

print(x)

#Character Type Testing These methods check the character content of a string. 

txt = "Company12"

x = txt.isalnum()

print(x)

txt = "CompanyX"

x = txt.isalpha()

print(x)

txt = "   "

x = txt.isspace()

print(x)

txt = "THIS IS NOW!"

x = txt.isupper()

print(x)

txt = "50800"

x = txt.isdigit()

print(x)