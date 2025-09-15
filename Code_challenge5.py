print("THE FACTORIAL PROGRAM")
number = eval(input("Enter any number---> "))

factorial = 0
for x in range(number,0, -1):
    #print(x)
    factorial *= x
print('The factorial of ',number,'is',factorial)