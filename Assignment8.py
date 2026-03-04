#Take positive and negative random numbers convert into labels positive and negative

numbers = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5]

for i in range(len(numbers)):
    if numbers[i] > 0:
        numbers[i] = "Positive"
    else:
        numbers[i] = "Negative"

print(numbers)