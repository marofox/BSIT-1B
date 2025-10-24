
#Fare Discount Calculator 

name = input("Enter your name -->")
fare = eval(input("Enter your fare -->"))
student = input("Are you a student?(yes/no)")

f = fare * 0.25


if student.lower() == 'yes':
	print("Hi",name,"\b!, Your discounted fare is ₱",f)
else:
	print("Hi",name,"\b!, Sorry sir/ma'am your not eligible for discount yout total fare is ₱",fare)
