#Ask the user to input the temperature
temp = input("Please enter the current temperature (°F): ")
#Convert the input string temperature to an integer
temp = int(temp)
#Set up the equality for the input temperature
if temp < 70:
    print ("Wear a jacket")
else:
    print ("No jacket required")
