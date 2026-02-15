# how a format method from string works
help(str.format)
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49.937678678))
txt = "For only {price} dollars!"
print(txt.format(price = '49.237678678'))
name = 'kishor'
age = 22
print('My name is:',name,'& my age is:',age)
name = 'kishor'
age = 22
print(f'My name is: {name} & my age is:{age}')
# i want next stamement on new line: use \n escapse sequence means new line
print(f'My name is: {name} \n& my age is:{age}')
# i want 4 spaces before name and age use \t means tab means 4 spaces
print(f'My name is:\t\t {name} \n& my age is:\t\t{age}')
name, id(name)  # id function gives a memory addess of an object
# print(*objects,sep=' ')
print(100,200,'python')
# change seperator
print(100,200,'python',sep='/')
# print(*object,sep=' ' ,end='\n')
print('Hello all')  # print default contains \n hence new statement goes to next line
print('Welcome')
print('Hello all',end='***')  # change end
print('Welcome')
