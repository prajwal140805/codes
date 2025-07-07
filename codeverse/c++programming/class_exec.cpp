#include <iostream>
#include <iomanip>
using namespace std;
class Car
{
public:
    // Data members
    string make;
    string model;
    int year;
    // Method to display car information
    void displayInfo()
    {
        cout << "Make:" << setw(15)<< setfill('-')  << make << endl
             << "Model:" << setw(14) << setfill('-') << model << endl
             << "Year:" << setw(15) << setfill('-') << year << endl;
    }
};

int main()
{
    Car myCar;
    // Assigning values to the data members of the object
    myCar.make = "Toyota";
    myCar.model = "Camry";
    myCar.year = 2023;
    // Calling the method of the object to display car information
    myCar.displayInfo();
    return 0;
}
