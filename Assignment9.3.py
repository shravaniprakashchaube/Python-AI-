# Question 3 - Filter Words with Length > 4 and Capitalize Them

names = ["shravani","falguni","rani"]

ans = list(
    map(lambda x: x.capitalize(),
        filter(lambda x: len(x) > 4, names))
)

print(ans)