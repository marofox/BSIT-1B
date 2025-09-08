#ask user to input temperature outside
#conditions as follow
# 0 to negative temperature --- BELOW FREEZING 
# 1 to 15 - Extreme Cold temperatures
# 16 to 30 - Cold Temperatures
# 31 to 38 - Lukewarm Temperatures
# 39 to 42 - Warm Temperatures
# 43 to 50 - Hot Temperature
# 51 to 60 - Extremely Hot Temperature
# 61 and above - Burning Temperature


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