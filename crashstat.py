#Name: Shaad Patankar
#Email: shaad.patankar73@myhunter.cuny.edu
#Date: October 30, 2023
#This program tells me the top three collision causes!

import pandas as pd

csvFile = input('Enter CSV file name: ')

tickets = pd.read_csv(csvFile)
print("The 3 biggest factors are:")
print(tickets["CONTRIBUTING FACTOR VEHICLE 1"].value_counts()[:3])