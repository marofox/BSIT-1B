depo=eval(input("Enter the amount you want to deposit:"))

ans1 = depo // 1000
sub1 = depo % 1000

ans2 = sub1 // 500
sub2 = sub1 % 500

ans3 = sub2 // 200
sub3 = sub2 % 200

ans4 = sub3 // 100
sub4 = sub3 % 100

ans5 = sub4 // 50
sub5 = sub4 % 50

ans6 = sub5 // 20
sub6 = sub5 % 20

ans7 = sub6 // 10
sub7 = sub6 % 10

ans8 = sub7 // 5
sub8 = sub7 % 5

ans9 = sub8 // 1
sub9 = sub8 % 1

print("Here is your breakdown to your deposit", depo)
print(ans1 ,"-₱1000") 
print(ans2 ,"-₱500")    
print(ans3 ,"-₱200") 
print(ans4 ,"-₱100") 
print(ans5 ,"-₱50") 
print(ans6 ,"-₱20") 
print(ans7 ,"-₱10") 
print(ans8 ,"-₱5") 
print(ans9 ,"-₱1")