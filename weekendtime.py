#Name: Shaad Patankar
#Email: shaad.patankar73@myhunter.cuny.edu
#Date: September 7, 2023
#This program tells me time till the weekend!

hours = int(input("How many hours till the weekend?: "))
days = hours // 24
hours = hours % 24

print(f"Days:{days}")
print(f"Hours:{hours}")