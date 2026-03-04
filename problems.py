"""
a = [(10,4),(2,3),(8,1),(4,5)]
#a.sort() # default it sorts in ascending order

a.sort(reverse=True) # sorts in descending order
# it is taking first element of the tuple as the key for sorting
print(a)
--------------------------------
a = [(10,4),(2,3),(8,1),(4,5)]
a.sort(key=lambda x:x[1]) 
print(a)
--------------------------------
a = [(10,4),(2,3),(8,1),(4,5)]
# x = []
# for val in a:
#     #print(val[0]+val[1])
#     #x.append(val[0]+val[1])
#     x.append(sum(val))
# print(x)
#----------------------------
# print([sum(val) for val in a])

# print(list(map(lambda x: x[0] + x[1], a)))
#-------------------------------
Pattern programs

1
12
123
1234
12345
"""
# for i in range(1,6):
#     for j in range(i):
#         print(i,'',end='')
#     print()


for i in range(1,6):
    for j in range(1,i+1): 
        print(i,'',end='')
    print()




