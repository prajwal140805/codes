#include <iostream>
#include <fstream>
using namespace std;

struct Time {
    int h, m, s;
};

int main() {
    Time t;

    cout << "Enter hour: ";
    cin >> t.h;
    cout << "minute: ";
    cin >> t.m;
    cout << "second: ";
    cin >> t.s;

    fstream file("time.dat", ios::out | ios::binary);
    file.write((char*)&t, sizeof(t));
    file.close();

    t = {0, 0, 0};

    file.open("time.dat", ios::in | ios::binary);
    file.read((char*)&t, sizeof(t));
    file.close();

    cout << "time is: " << t.h << ":" << t.m << ":" << t.s << endl;

    return 0;
}
