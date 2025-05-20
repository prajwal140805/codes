#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    float x = 6.28;
    float y = -3.142;
    float z;
    z = max(x, y);
    cout << z << '\n';
    z = min(x, y);
    cout << z << '\n';
    z = pow(x, y);
    cout << z << '\n';
    z = sqrt(y);
    cout << z << '\n';
    z = abs(y);
    cout << z << '\n';
    z = round(y);
    cout << z << '\n';
    z = ceil(y);
    cout << z << '\n';
    z = floor(y);
    cout << z << '\n';

    return 0;
}