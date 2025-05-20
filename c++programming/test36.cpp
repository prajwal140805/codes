// Design a class called Gadget with member functions to operate gadgets. Derive classes Phone and Tablet from Gadget. Additionally, derive a class called SmartDevice from
#include <iostream>
using namespace std;
class gadget
{
public:
    void operate()
    {
        cout << "use battery to operate" << endl;
    }
};
class phone : public gadget
{
public:
    void call()
    {
        cout << "phone used to make calls" << endl;
    }
};
class tablet : public gadget
{
public:
    void browse()
    {
        cout << "use to browse internet" << endl;
    }
};
class smartphone : public phone, public tablet
{
public:
    void displaydetails()
    {
        cout << "smartphone used to make calls and browse internet and operate like a gadget" << endl;
    }
};
int main()
{
    smartphone s1;
    s1.displaydetails();
    s1.browse();
    s1.call();
    s1.phone::operate();
    s1.tablet::operate();
    return 0;
}