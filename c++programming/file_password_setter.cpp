#include <iostream>
#include <fstream>
using namespace std;
string pass, orgpass;
int func;

void main2();

void openfile()
{

    int i = 0;
    do
    {
        cout << "Enter the password: ";
        cin >> pass;
        system("cls");
        cout << endl
             << endl
             << endl;
        if (pass == orgpass)
        {
            cout << "Access granted to files:" << endl;
            cout << "*****files opened*****" << endl
                 << endl
                 << endl;

            ifstream file("data.txt");
            if (file.is_open())
            {
                string line;
                while (getline(file, line))
                {
                    cout << line << endl;
                }
                file.close();
            }
            else
            {
                cout << "Error: Could not open file." << endl;
            }
            main2();
        }
        else
        {

            cout << "*****Invalid password*****" << endl
                 << endl
                 << endl;
            cout << "press 1 to try again:" << endl;
            cout << "press 3 to exit:" << endl;
            cin >> i;
            system("cls");
            if (i == 3)
                main2();
        }
    } while (i == 1);
}

void resetpassword()
{

    int i = 0;
    do
    {
        cout << "enter your old password:" << endl;
        cin >> pass;
        system("cls");
        if (pass == orgpass)
        {
            cout << "enter your new password:" << endl;
            cin >> pass;
            system("cls");
            if (pass == orgpass)
            {
                cout << "*****Invalid password*****" << endl;
                cout << "press 1 to try again:" << endl;
                cout << "press 3 to exit:" << endl;
                cin >> i;
                system("cls");
                if (i == 3)
                    main2();
            }
            else
            {
                orgpass = pass;
            }
            cout << "Password reset successfully:" << endl
                 << endl
                 << endl;
            main2();
        }
        else
        {

            cout << "*****Invalid password*****" << endl;
            cout << "press 1 to try again:" << endl;
            cout << "press 3 to exit:" << endl;
            cin >> i;
            system("cls");
            if (i == 3)
                main2();
        }
    } while (i == 1);
}

void exit()
{
    cout << "*****exiting*****" << endl;
    return;
}

void notvalid()
{

    cout << "*****Invalid option*****" << endl;
    main2();
}

void main2()
{

    cout << "enter among the following options: " << endl;
    cout << "1-open files ;" << endl;
    cout << "2-reset your password ;" << endl;
    cout << "3-exit ;" << endl;
    cin >> func;
    system("cls");
    if (func == 1)
        openfile();
    else if (func == 2)
        resetpassword();
    else if (func == 3)
        exit();
    else
        notvalid();
}

int main()
{
    system("cls");
    cout << "set your password: ";
    cin >> orgpass;
    system("cls");
    cout << "Password set successfully:" << endl
         << endl
         << endl;
    main2();
}
