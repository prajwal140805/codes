#include <iostream>
#include <cmath>
using namespace std;
int main()
{
    int x, y,result;
    char op;
    system("cls");
    cout << "Enter:\n";
    cin >> x;
    cin >> op;
    cin >> y;

    switch (op)
    {
    case '+':
        result = x + y;
        cout << x<<'+'<<y<<'=' << result;
        break;
    case '-':
        result = x - y;
        cout << x<<'-'<<y<<'=' << result;
        break;
    case '*':
        result = x * y;
        cout << x<<'*'<<y<<'=' << result;
        break;
    case '/':
        result = x / y;
        cout << x<<'/'<<y<<'=' << result;
        break;
    case 'p':
        result = pow(x, y);
        cout << '('<<x<<')'<<'^'<<y<<'=' << result;
        break;
    case '%':
        result = x % y;
        cout  << x<<'%'<<y<<'=' << result;
        break;
    default:
        cout << "enter the valid operator";
    }
    cout << "Calculation done! Press Enter to clear and continue...\n";
cin.ignore();
cin.get();
system("cls");

    return 0;
}