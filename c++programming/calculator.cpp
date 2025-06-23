#include <iostream>
#include <cmath>
using namespace std;
int main()
{
    int x, y, result;
    char op;
    cout << "Enter the first number:\n";
    cin >> x;
    cout << "enter the operator among +,-,*,/,%(modulo oprt),p(power):" << '\n';
    cin >> op;
    cout << "Enter the second number:\n";
    cin >> y;

    switch (op)
    {
    case '+':
        result = x + y;
        cout << "The result is :" << result;
        break;
    case '-':
        result = x - y;
        cout << "The result is :" << result;
        break;
    case '*':
        result = x * y;
        cout << "The result is :" << result;
        break;
    case '/':
        result = x / y;
        cout << "The result is :" << result;
        break;
    case 'p':
        result = pow(x, y);
        cout << "The result is :" << result;
        break;
    case '%':
        result = x % y;
        cout << "The result is :" << result;
        break;
    default:
        cout << "enter the valid operator";
    }
    return 0;
}