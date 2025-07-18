#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;

struct Time {
    int h, m, s;
};

int main() {
    Time t;

    cout << "Enter hour: ";
    cin >> t.h;
    cout << "Enter minute: ";
    cin >> t.m;
    cout << "Enter second: ";
    cin >> t.s;

    fstream file;
    file.open("time.dat", ios::out | ios::binary);
    file.write((char*)&t, sizeof(t));
    file.close();

    t = {0, 0, 0};

    file.open("time.dat", ios::in | ios::binary);
    file.read((char*)&t, sizeof(t));
    file.close();

    cout << "time is: "<<setw(2)<<setfill('0') << t.h << ":"<<setw(2) <<setfill('0')<< t.m << ":" <<setw(2)<<setfill('0')<< t.s << endl;

    return 0;
}
