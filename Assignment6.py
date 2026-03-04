#can we pass multiple values through return?

# Yes, Python actually returns them as a tuple by default.

def student_details():
    name = "Shravani"
    age = 25
    city = "Sangli"
    return name, age, city   # multiple values

data = student_details()
print(data)