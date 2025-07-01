#include <iostream>
#include <fstream>
using namespace std;

struct Time {
    int h, m, s;
};

int main() {
    Time t;

    cout << "Enter hour, minute, second: ";
    cin >> t.h >> t.m >> t.s;

    fstream file("time.dat", ios::out | ios::binary);
    file.write((char*)&t, sizeof(t));
    file.close();

    t = {0, 0, 0}; // reset

    file.open("time.dat", ios::in | ios::binary);
    file.read((char*)&t, sizeof(t));
    file.close();

    cout << "Read time: " << t.h << ":" << t.m << ":" << t.s << endl;

    return 0;
}
