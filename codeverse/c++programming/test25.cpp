#include <iostream>
using namespace std;

int main() {
    float basicSalary, dearnessAllowance, houseRentAllowance, grossSalary;

    // Taking input
    cout << "Enter Vivek's basic salary: $";
    cin >> basicSalary;

    // Calculating allowances
    dearnessAllowance = 0.40 * basicSalary;
    houseRentAllowance = 0.20 * basicSalary;

    // Calculating gross salary
    grossSalary = basicSalary + dearnessAllowance + houseRentAllowance;

    // Displaying the result
    cout << "\n--- Salary Details ---\n";
    cout << "Basic Salary: $" << basicSalary << endl;
    cout << "Dearness Allowance (40%): $" << dearnessAllowance << endl;
    cout << "House Rent Allowance (20%): $" << houseRentAllowance << endl;
    cout << "Gross Salary: $" << grossSalary << endl;

    return 0;
}
