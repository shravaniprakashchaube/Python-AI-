# map and filter based questions 
# question4 - Filter Numbers Between 10 and 50 and Double Them

num = [5,15,25,6,36,7,14]

ans = list(
    map(lambda x: x*2,
    filter(lambda x: 10 <= x <= 50 ,num)     )




)
print(ans)