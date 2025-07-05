#include <iostream>
#include <fstream>
#include <conio.h>

using namespace std;
string pass, ch, keypass, orgpass;
fstream file;
int func;
char digit;
char arr[100];
int i = 0;

void main2();
void exit();

void openfile()
{
    int i;
    do
    {
        cout << "Enter the password: ";
        cin >> pass;

        system("cls");
        cout << endl
             << endl
             << endl;
        if (pass == keypass)
        {


            ifstream file("data.txt");
            if (file.is_open())
            {
            cout << "*****files opened*****" << endl
                 << endl
                 << endl;
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

            cout << "Error: Invalid password!!" << endl
                 << endl
                 << endl;
            cout << "press 1 to try again:" << endl;
            cout << "press 2 to go back:" << endl;
            cout << "press 3 to exit:" << endl;
            i = getch() - '0';

            system("cls");
            if (i == 2)
                main2();
            if (i == 3)
                exit();
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
        if (pass == keypass)
        {
            cout << "enter your new password:" << endl;
            cin >> pass;
            system("cls");
            if (pass == keypass)
            {
                cout << "Error:New password cannot be same as the old one!!" << endl;
                cout << "press 1 to try again:" << endl;
                cout << "press 2 to go back:" << endl;
                cout << "press 3 to exit:" << endl;
                i = getch() - '0';
                system("cls");
                if (i == 2)
                 main2();
                if (i == 3)
                    exit();
            }
            else
            {
                file.open("password.txt", ios::out);
                if (!file)
                {
                    system("cls");
                    cout << "Error: Not able to set password!!!";
                }
                else
                {

                    cout << "Password Reset Successfully:" << endl
                         << endl
                         << endl;
                    file << pass;
                    file.close();
                    main2();
                }
            }
        }
        else
        {
            cout << "Error: Invalid password!!" << endl;
            cout << "press 1 to try again:" << endl;
            cout << "press 2 to go back:" << endl;
            cout << "press 3 to exit:" << endl;
            i = getch() - '0';
            system("cls");
            if (i == 2)
                main2();
            if (i == 3)
                exit();
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

    cout << "Error:Invalid option" << endl;
    main2();
}

void main2()
{

    cout << "enter among the following options: " << endl;
    cout << "1-open files" << endl;
    cout << "2-reset your password" << endl;
    cout << "3-exit" << endl;
    func = getch() - '0';
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
    file.open("password.txt", ios::in);
    bool key = (file.peek() == std::ifstream::traits_type::eof() ? 1 : 0);
    file.close();

    if (key == 1)
    {
        file.open("password.txt", ios::out);
        system("cls");
        cout << "set your password: ";
        cin >> orgpass;
        system("cls");
        if (!file)
        {
            system("cls");
            cout << "Error:not able to set password!!!";
        }
        else
        {

            cout << "Password set successfully:" << endl
                 << endl
                 << endl;
            file << orgpass;
            file.close();
        }
    }
    else
    {
        system("cls");
    }
    file.open("password.txt", ios::in);
    while (file >> digit)
    {
        arr[i++] = digit;
    }
    file.close();
    keypass = string(arr, i);
    main2();
}
