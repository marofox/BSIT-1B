#ask the user to input ten(10) numbers
#after get the summation of all numbers
sum = 0
for x in range(1, 11, 1):
    num = eval(input("Enter any number --> "))
    sum += num
print("The sum of all given numbers is", sum)
