# map and filter based questions 
# question5 - Filter Numbers Ending with 5 and Multiply by 2

num = [15, 23, 35, 40, 55, 60]

ans  = list(
    map(lambda x: x * 2,
        filter(lambda x: str(x).endswith("5"), num))
)

print(ans)

