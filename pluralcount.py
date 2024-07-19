#Name: Shaad Patankar
#Email: shaad.patankar73@myhunter.cuny.edu
#Date: September 28, 2023
#This program counts plurals!

s = input("Enter nouns: ")
words = (s.count(" ") + 1)
print(f"Number of words:  {words}")
plurals = (s.count("s "))
if s[-1] == "s":
    plurals += 1
print(f"Fraction of your list that is plural is {(plurals/words)}")

