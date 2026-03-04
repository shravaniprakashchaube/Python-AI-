# map and filter based questions 
# question1 - Filter even numbers and square them

num = [1,2,3,4,5,6,7]
ans = list(
    map(lambda x: x**2,
    filter(lambda x: x % 2 == 0, num))
)

print(ans)