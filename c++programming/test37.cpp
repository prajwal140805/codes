/* Write a base class called Fruit with member functions to get and set the fruit's color. Derive classes Apple and Banana from Fruit. Implement member functions to displ*/
#include <iostream>
using namespace std;
class Fruit
{
protected:
    string color;

public:
    void setColor(string c)
    {
        color = c;
    }
    string getColor()
    {
        return color;
    }
};
class Apple : public Fruit
{
public:
    void displayDetails()
    {
        cout << "This apple is " << getColor() << "." << endl;
    }
};
class Banana : public Fruit
{
public:
    void displayDetails()
    {

        cout << "This banana is " << getColor() << "." << endl;
    }
};
int main()
{
    Apple apple;
    Banana banana;
    apple.setColor("red");
    banana.setColor("yellow");
    apple.displayDetails();
    banana.displayDetails();
    return 0;
}