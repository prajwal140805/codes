#include <iostream>
using namespace std;

int main() {
    int a,b;
    a = 100;
    cin >> a;
    int temp = 0; // Initialize temp to 0

    while (a > 0) {
        int digit =a % 10; // Extract the last digit
        temp = temp * 10 + digit; // Append the digit to the reversed number
        a = a / 10; // Remove the last digit
    }

    cout << temp << endl;

    return 0;
}