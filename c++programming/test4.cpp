#include <iostream>
using namespace std;
int factorial(int n);
int main()
{
    int n;
    int result;
    cout << "Enter the number to find the factorial: ";
    cin >> n;
    result = factorial(n);
    cout << result;
    return 0;
}
int factorial(int n)
{
    if (n == 0)
    {
        return 1;
    }
    return n * factorial(n - 1);
}