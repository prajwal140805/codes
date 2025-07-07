#include <iostream>
#include <string>
using namespace std;

class car {
public:
    string brand;
    string model;
    int year;
    string color;
    int speed;

    void setbrand(string b) {
        brand = b;
    }
    void setmodel(string m) {
        model = m;
    }
    void setyear(int y) {
        year = y;
    }
    void setcolor(string c) {
        color = c;
    }
    void setspeed(int s) {
        speed = s;
    }
    void setprice(int p) { // Made public
        price = p;
    }
    int prajwal() const {
        return price;
    }

private:
    int price;
};

int main() {
    car c1;
    string b, m, c;
    int y, s, p;

    // Accept car details from the user
    cout << "Enter the brand of the car: ";
    cin >> b;
    cout << "Enter the model of the car: ";
    cin >> m;
    cout << "Enter the year of the car: ";
    cin >> y;
    cout << "Enter the color of the car: ";
    cin >> c;
    cout << "Enter the speed of the car: ";
    cin >> s;
    cout << "Enter the price of the car: ";
    cin >> p;
    

    // Set the car details
    c1.setbrand(b);
    c1.setmodel(m);
    c1.setyear(y);
    c1.setcolor(c);
    c1.setspeed(s);
    c1.setprice(p);

    // Display the car details
    cout << "Car Details:" << endl;
    cout << "Brand: " << c1.brand << endl;
    cout << "Model: " << c1.model << endl;
    cout << "Year: " << c1.year << endl;
    cout << "Color: " << c1.color << endl;
    cout << "Speed: " << c1.speed << endl;
    cout << "Price: " << c1.prajwal() << endl;

    return 0;
}