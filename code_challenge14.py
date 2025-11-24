import os
import json
os.system('cls')
print("Student Information System")
print("================================")

#empty dictionary

student_record = {}

while True:

    print("A - add student record ")
    print("B - print all student record ")
    print("C - search student record ")
    print("D - delete student record ")
    print("E - edit student record ")
    print("F - export student record ")
    print("G - import student record ")
    print("X - sytem Exit ")

    choice = input("select from the action above---->").lower()

    if choice == 'a':
        os.system('cls')
        print("\nAdding student record")
        id_no = input("please input your student id number ")
        first_name = input("please input your first name ")
        last_name = input("please input your last name ")
        age = eval(input("please input your age "))
        section = input("please input your section ")

        student_record[id_no] = [first_name,last_name,age,section]
        print("DATA SAVED SUCCESSFULLY")
        continue
    elif choice == 'b':
        os.system('cls')
        print('print student record')
        #print (student record) simple approach
        for m, n in student_record.items():#key - values
            print(f"STUDENT ID - {m}, Informtion - {n}")
        continue
    elif choice == 'c':
        os.system('cls')

        print("SEARCH STUDENT RECORD")

        search_id = input("Input student Id for search").lower()#lowercase letter
        
        for each_id in student_record.keys():
            if search_id in student_record.keys():
                print("============================")
                print(f'Record Found for ID{search_id}')
                for m in student_record[search_id]:
                    print(f'----{m}')#f = means format
                print("+++++++++++++++++++++++++++++++")
                print("\n\RECORD FOUND")
            else:
                print("NO RECORD FOUND")
            break
        continue
    elif choice == 'd':
        os.system('cls')
        print("SEARCH STUDENT RECORD")

        search_id = input("Input student Id for search").lower()#lowercase letter
        
        for each_id in student_record.keys():
            if search_id in student_record.keys():
                print("============================")
                print(f'Record Found for ID{search_id}')
                for m in student_record[search_id]:
                    print(f'----(m)')#f = means format
                print("+++++++++++++++++++++++++++++++")
                #.pop() = means to delete an item
                student_record.pop(search_id)
                print("\n\RECORD FOUND")
            else:
                print("NO RECORD FOUND")
            break
        continue
    elif choice == 'e':
        os.system('cls')

        print("EDIT/MODIFY STUDENT RECORD")

        search_id = input("INPUT STUDENT ID FOR SEARCH ---> ").lower()
        for each_id in student_record.keys():
            print("===================================")
            print(f"\nRECORD FOUND FOR ID {search_id}")
            #PARA MA RPINT YUNG RECORD PARA SA SEARCH ID
            for m in student_record[search_id]:
                print(f"---- (m)")
            print("=================================")
            #bagong set ng value para sa search id
            first_name = input("PLEASE INPUT STUDENT FIRST NAME -----> ").upper()#papalakihin ang letter
            second_name = input("Please input Student Second name ----> ").upper()
            age = eval(input("Input student age ---> "))
            course = input("Input student course ----> ").upper()
            section = input("Input student section ----> ").upper()

            student_record[search_id][0] = first_name
            student_record[search_id][1] = second_name
            student_record[search_id][2] = age
            student_record[search_id][3] = course
            student_record[search_id][4] = section  
            
            print("RECORD UPDATED")

        else:
                print("NO RECORD FOUND")
        break
        continue
    elif choice == 'f':
        os.system('cls')
        print("EXPORT STUDENT DATA ")# ita transfer ang data
        #json java script object notation

        with open('student_records.json', 'w') as new_file:
            json.dump(student_record,new_file, indent=4 )

        print("\n\nDATA EXPORTED TO JSON")
        continue
    elif choice == 'g':
        os.system('cls')
        print("import student data ") #ilalagay ang data 
        # R- means read and W- means write
        with open('student_records.json', 'r') as new_file:
            import_student = json.load(new_file)

        student_record = import_student
        print("\n\nDATA AY NAIMPORT NA")
        continue
    elif choice == 'x':
        print("SYSTEM ALIS")    
        break
    else:
        print("INVALID CHOICE, RE ENTER YOUR CHOICE")
        continue
