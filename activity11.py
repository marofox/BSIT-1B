temp = eval(input("input temperature outside ---> ",))
#1 to 15
if temp <=0 : 
	print("temperature if considered as Below Freezing")
elif temp <=1 and temp <= 15: 
	print("temperature if considered as extremely cold")
elif temp <=16 and temp <= 30: 
	print("Cold Temperatures")
elif temp <=31 and temp <= 38: 
	print("Lukewarm Temperatures")
elif temp <=39 and temp <= 42: 
	print("Warm Temperatures")
elif temp <=43 and temp <= 50: 
	print("Hot Temperature")
elif temp <=51 and temp <= 60: 
	print("Extremely Hot Temperature")
elif temp >=61: 
	print("Burning Temperature")

else: 
	print("invalid temperature")