//#Name: Shaad Patankar
//#Email: shaad.patankar73@myhunter.cuny.edu
//#This program prints a triangle!

#include <iostream>
using namespace std;

int main()
{
    int n; // the number entered by the user
    cout << "Enter a whole number between -31 and 31: ";
    cin >> n;

    // check if the number is valid
    if (n < -31 || n > 31)
    {
        cout << "Invalid number. Program terminated.\n";
        return 0;
    }

    int x; // the number to be converted to two's complement
    if (n < 0) // if the number is negative
    {
        cout << "1"; // print a 1
        x = 32 + n; // let x = 32 + n
    }
    else // if the number is not negative
    {
        cout << "0"; // print a 0
        x = n; // let x = n
    }

    int b = 16; // the base to divide by
    while (b > 0.5) // while b is positive
    {
        if (x >= b) // if x is greater than or equal to b
        {
            cout << "1"; // print a 1
            x = x % b; // let x be the remainder of dividing x by b
        }
        else // if x is less than b
        {
            cout << "0"; // print a 0
        }
        b = b / 2; // let b be half of b
    }

    cout << "\n"; // print a new line

    return 0;
}


