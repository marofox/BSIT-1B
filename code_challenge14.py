print("Student Information System")
print("================================")

#empty dictionary

student_record = {}

while True:

    print("A - add student record")
    print("B - print all student record")
    print("C - search student record")
    print("D - delete student record")
    print("E - edit student record")
    print("F - export student record")
    print("G - exit system")

    choice = input("select from the action above---->").lower()

    if choice == 'a':
        os.system('cls')
        print("\nAdding student record")
        id_no = input("please input your student id number")
        first_name = input("please input your first name")
        last_name = input("please input your last name")
        age = eval(input("please input your age"))
        section = input("please input your section")

        student_record[id_no] = [first_name,last_name,age,section]
        print("DATA SAVED SUCCESSFULLY")
        continue
    elif choice == 'a':
        pass
        continue
    elif choice == 'c':
        pass
        continue
    elif choice == 'd':
        pass
        continue
    elif choice == 'e':
        pass
        continue
    elif choice == 'f':
        pass
        continue
    elif choice == 'g':
        print("Exit system")
        break
    else:
        print('invalid input')
        continue