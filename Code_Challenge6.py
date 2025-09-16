print('Odd Number Summation')

a = 0

for b in range(1, 8, 1):
    c = eval(input('Input Ramdom Number --> '))
    if c % 2:
        a += c

print("Summation of all odd number:",a)
