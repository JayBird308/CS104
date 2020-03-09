#Prints a message prompting the user followed by a variable asking for user input
print("Please enter your last name,first name,favorite color,favorite animal,favorite team: ")
#There's nothing in "Input()" because we are waiting for it to be entered by the user through python initializer, user String is just a string variable name, it can be changed to anything as long as it matches the rest of the code
userString = input()

#stores the location of commas so we know where to seperate the words in the list later (there's 4 commas so c1 is the first comma after the last name). c2-c4 are a little different because the find command finds the FIRST comma by default.
#So, the c1+1 or c2+2 pretty much says I want  the first comma after c1 or the second comma after c2
c1 = userString.find(",")
c2 = userString.find(",",c1 + 1)
c3 = userString.find(",",c2 + 2)
c4 = userString.find(",",c3 + 3)

#stores the length of the input so we can use it for the bound at the end of the string, since there is no comma at the end, how will we know where to stop chopping the pieces? Well, we will use the total length of the string as the end index
userStringLength = len(userString)

#extracts last name from main string (from beginning (0) to the first comma (c1))
lastName = userString[0:c1]

#extracts first name from main string (from first comma +1 (becuase we dont want ",Name" we want "Name") to the second comma)
firstName = userString[c1+1:c2]

#extracts favorite color (same as last step)
favColor = userString[c2+1:c3]

#extracts favorite animal (same as last step)
favAnimal = userString[c3+1:c4]

#extracts favorite team (So, here we want the substring from the last comma +1 to the total length (the end of the string))
favTeam = userString[c4+1:userStringLength]

#Now we set up a print function to match what the requirements from the assignment were, but instead of manually typing in the answers, we fill it in with the variable names, and so everything in green is printed literally and the variables are in black (which can change based on what is typed into userString)
print("My name is " + firstName + " " + lastName + ", my favorite color is " + favColor + ", my favorite animal is a " + favAnimal + ", and my favorite team is the " + favTeam)

