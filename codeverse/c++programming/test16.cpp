#include <iostream>
#include <vector>
using namespace std;

class Car {
public:
    string model;
    int year;
    double rentPerDay;
    bool isAvailable;

    Car(string m, int y, double r) : model(m), year(y), rentPerDay(r), isAvailable(true) {}

    void rentCar() {
        if (isAvailable) {
            isAvailable = false;
            cout << model << " has been rented." << endl;
        } else {
            cout << model << " is already rented." << endl;
        }
    }

    void returnCar() {
        if (!isAvailable) {
            isAvailable = true;
            cout << model << " has been returned." << endl;
        } else {
            cout << model << " was not rented." << endl;
        }
    }

    void display() {
        cout << "Model: " << model << ", Year: " << year << ", Rent/Day: $" << rentPerDay
             << ", Available: " << (isAvailable ? "Yes" : "No") << endl;
    }
};

int main() {
    vector<Car> cars = {Car("Toyota Corolla", 2020, 50), Car("Honda Civic", 2019, 45), Car("Ford Focus", 2021, 60)};

    cout << "Available cars:" << endl;
    for (auto& car : cars) {
        car.display();
    }

    cars[0].rentCar();
    cars[0].returnCar();
    cars[1].rentCar();

    cout << "\nUpdated car list:" << endl;
    for (auto& car : cars) {
        car.display();
    }

    return 0;
}