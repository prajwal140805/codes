#include <iostream>
#include <stdexcept>
using namespace std;

int main()
{ string name;
   try{
  
    do
    {
        cout << "enter your name:";
        getline(cin, name);
        
    } while (name.empty());
if (name.length() < 3)
    {
        throw 5;
    }}
    catch (int x)
    {
        cout << "Name must be at least 3 characters long." << endl;
        return 1;
    }

    cout << "welcome " << name << ", this is the world of codes";
    return 0;
}