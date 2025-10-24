for x in range(1, 10,1):
    for i in range(10, x, -1):
        print(" ", end=" ")
    for b in range(x, 0, -1):
        print(b,end=" ")
    for v in range(2, x+1, 1):
        print(v,end=" ")
    print()
