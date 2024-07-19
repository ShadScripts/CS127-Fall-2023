#Name: Shaad Patankar
#Email: shaad.patankar73@myhunter.cuny.edu
#Date: November 2, 2023
#This program asks the user for a non-empty string and then prints it!

empty = ""
userstring = ""

while userstring == empty:
    userstring = input("Enter a non-empty string: ")
    print("That was empty. Try again.")

print(userstring)