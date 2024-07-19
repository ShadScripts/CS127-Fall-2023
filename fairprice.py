#Name: Shaad Patankar
#Email: shaad.patankar73@myhunter.cuny.edu
#Date: October 30, 2023
#This program makes a computes fare!

offpeak = [6.25, 7.5, 7.5, 8.75, 9.75, 9.75, 9.75]

peak = [8.75, 10.25, 10.25, 12.00, 13.50, 13.50, 13.50]


def computeFare(zone, type):
    if zone >= 8:
        return -1
    elif type == "peak":
        return(peak[zone-1])
    else:
        return(offpeak[zone-1])
x = input('zone')
y = input('type')

computeFare(x,y)