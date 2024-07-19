#Name: Shaad Patankar
#Email: shaad.patankar73@myhunter.cuny.edu
#Date: Oct 27, 2023
#A program that uses functions to print out months.

def monthString(monthNum):
    monthString = ""
    months = ['January','February','March','April','May','June',
              'July','August','September','October','November','December']
    monthString = months[monthNum-1]
    return (monthString)


def main():
    n = int(input('Enter the number of the month: '))
    mString = monthString(n)
    print('The month is', mString)


# Allow script to be run directly:
if __name__ == "__main__":
    main()
