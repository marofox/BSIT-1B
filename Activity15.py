fname = 'Mar'
lname = 'Las Piñas'
print(f"My full name is {fname} {lname}")

fname = 'Sam'
lname = 'Sio'
print(f"My full name is {fname.upper()} {lname.upper()}")

sum = 0 
for i in range(1, 6):
    x  = eval(input(f"{i} - Input a number --> "))
    sum += x 
print(f"The total sum is {sum}")
