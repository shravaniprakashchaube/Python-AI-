# map and filter based questions 
# question2 - Filter Positive Numbers and Add 10

num = [-1,-2,-3,4,5,6,7]
ans = list(
    map(lambda x: x+10,
    filter(lambda x: x >0 == 0, num))
)

print(ans)
