#include <iostream>
#include <fstream>
using namespace std;
int main()
{ fstream file;
    while (true)
    {file.open("sample.txt", ios::out|ios::app );
    if (!file)
    {
        cout << "Error in creating file!!!" << endl;
        return 0;
    }
    else
    {
        cout << "File created successfully." << endl;
    }
     file << "This is a sample text file." << endl;
      
    file.close();

    file.open("sample.txt", ios::in);
    if (!file)
    {
        cout << "Error in opening file!!!" << endl;
        return 0;
    }

    char ch;
    cout << "File content: " << endl;
    while (file >> noskipws >> ch)  // read noskipws ensures spaces are read
    {
        
        {
            cout << ch;
        }
    }

    file.close();}
   
    
    return 0;
}
