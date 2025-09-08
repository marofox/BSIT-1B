#ask user for an item price
#quantity
#if cost is above 100, apply dsicount of 10%

price = eval(input("input item price --> "))
quantity = eval(input("item quality --> "))

cost = price * quantity

if cost >=100:
	discount = cost * 0.10
	final_cost = cost - discount
	print ("discount price is ", final_cost)
else:
	print("no discount applird, costis ", cost)