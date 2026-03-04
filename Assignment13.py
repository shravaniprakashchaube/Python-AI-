# Take a cart with some amount [1999,599,299,100,500,2111,3999]
# i want to process products >500 with 70 rs of delivery charge

cart = [1999,599,299,100,500,2111,3999]

products = filter(lambda x: x > 500,cart)
total_amount = list(map(lambda x: x+70,products))
print(total_amount)