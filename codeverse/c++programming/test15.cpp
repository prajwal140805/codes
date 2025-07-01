#include <iostream>
using namespace std;
 
void isPrime(int& num, bool& result) {
    if (num <= 1) {
        result = false;  
        return;
    }
    result = true;  
    for (int i = 2; i <= num / 2; i++) {
        if (num % i == 0) {
            result = false;  
        }
    }
}

int main() {
    int number;
    bool prime;
    cout << "Enter a number: ";
    cin >> number;

    isPrime(number, prime);

    if (prime) {
        cout << number << " is a prime number." << endl;
    } else {
        cout << number << " is not a prime number." << endl;
    }

    return 0;
}