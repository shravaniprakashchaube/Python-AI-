#check all methods of set 

#add()

languages = {"python,java,c"}
languages.add("c++")
print(languages)

#clear()
languages = {"python,java,c"}
languages.clear()
print(languages)

#copy()
languages = {"python,java,c"}
l = languages.copy()
print(l)

#difference
#Return a set that contains the items that only exist in set x, and not in set y

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y)
print(z)

#discard()

languages = {"english", "hindi", "marathi"}
languages.discard("english")
print(languages)

#update()
x = {"A", "B", "C"}
y = {"B", "C", "D"}
x.update(y) 
print(x)

#union()
#Return a set that contains all items from both sets, duplicates are excluded
x = {"AA", "BB", "CC"}
y = {"BB", "CC", "DD"}
z = x.union(y) 
print(z)
