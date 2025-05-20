#include <iostream>
class circle {
    private:
        int radius;
        const double pi = 3.14;

    public:
        // Function to set the radius
        void setradius(int r) {
            radius = r;
        }

        // Function to calculate the area of the circle
        double getarea() const {
            return pi * radius * radius;
        }
};

int main() {
    circle c1;
    int r;

    // Accept radius from the user
    std::cout << "Enter the radius of the circle: ";
    std::cin >> r;

    // Set the radius and calculate the area
    c1.setradius(r);
    std::cout << "The area of the circle is: " << c1.getarea() << std::endl;

    return 0;
}

