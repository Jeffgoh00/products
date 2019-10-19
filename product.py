products = []

while True:
	name = input ("Fil in the product name: ")
	if name == "q":
		break
	price = input ("Fill in the product price: ")
	products.append([name, price])
print(products)

for p in products:
	print(p[0], "price is", p[1])