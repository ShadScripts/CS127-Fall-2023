//Name:  Shaad Patankar
//Email:  SHAAD.PATANKAR73@myhunter.cuny.edu
//Date:  December 7 2023
//Prints "Mihi cura futuri" 10 times, using a loop

#include <iostream>
using namespace std;

int main()
{
    // Declare a variable to store the number of kilometers
    double kilometers;

    // Prompt the user for the number of kilometers
    cout << "Enter the number of kilometers: ";
    cin >> kilometers;

    // Convert kilometers to miles using the formula: 1 km = 0.621371 miles
    double miles = kilometers * 0.621371;

    // Print out the number of miles
    cout << miles << " miles." << endl;

    return 0;
}
