#include <iostream>
#include <string>
using namespace std;

void numberToCharacters(int num) {
    string str = to_string(num);
    for (char c : str) {
        cout << c << " ";
    }
    cout << endl;
}

int main() {
    int number;
    cout << "Enter a number: ";
    cin >> number;

    numberToCharacters(number);
    return 0;
}