
for x in range(1, 11,1):
    for i in range(10, x, -1):
        print(" ", end=" ")
    for b in range(1, x, 1):
        print('*',end=" ")
    for c in range(1, x, 1):
        print("*",end=" ")
    print()

for x in range(1, 11,1):
    for i in range(1, x, 1):
        print(" ", end=" ")
    for b in range(10, x, -1):
        print('*',end=" ")
    for c in range(10, x, -1):
        print("*",end=" ")
    print()
