// Write a base class called Animal with a virtual function eat().Derive classes Herbivore and Carnivore from Animal and override the eat() function in each derived
#include <iostream>
using namespace std;
// Base class
class Animal
{
public:
    virtual void eat()
    { // Virtual function
        cout << "Animal is eating..." << endl;
    }
};
// Derived class Herbivore
class Herbivore : public Animal
{
public:
    void eat() override
    { // Overriding the virtual function
        cout << "Herbivore is eating plants." << endl;
    }
};
// Derived class Carnivore
class Carnivore : public Animal
{
public:
    void eat() override
    { // Overriding the virtual function
        cout << "Carnivore is eating meat." << endl;
    }
};
int main()
{
    // Creating objects of derived classes
    Herbivore herbivore;
    Carnivore carnivore;
    // Demonstrating virtual function behavior
    Animal *a1 = &herbivore; // Pointer to Herbivore
    Animal *a2 = &carnivore; // Pointer to Carnivore
    a1->eat();               // Calls Herbivore's eat()
    a2->eat();               // Calls Carnivore's eat()
    return 0;
}