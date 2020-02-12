#Ask the user to input the temperature
temp = input("Please enter the current temperature (°F): ")
#Convert the input string temperature to an integer
temp = int(temp)
#Set up the equality statement for the input temperature
if temp >= 70:
    print ("No jacket required")
else:
    print ("Wear a jacket")
