#while loop
#laundry analogy
#keywords -- while,continue,break
#requirements - boolean initial value

isneat = True #boolean initial value
cycle = 0
while isneat == True:
    confirm = input("do you want to continue washing(yes/no)").lower()
    cycle += 1
    if confirm == 'yes':
        print("washing continues ....")
        continue
    else:
        print("stop washing ....")
        break
print("the number if cycle is", cycle - 1)
    
