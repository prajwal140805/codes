#include <iostream>
#include <ctime>
using namespace std;

char guc();
char gcc();
void sc(char choice);
void cw(char player, char computer);

int main()
{
    char player;
    char computer;
    cout << "rock-paper-scissors Game!" << endl;
    cout << "choose one of the following\n r for rock\n p for paper\n s for scissors\n q to quit\n ";
    while (true)
    {
        player = guc();
        
         if (player == 'q')
        {
            cout << "Exiting the game. Goodbye!" << endl;
            break;
        }
        cw(player, computer);
        cout << "your choice: ";
        sc(player);
        computer = gcc();
        cout << "computer's choice: ";
        sc(computer);
        
       
    }

    return 0;
}

char guc()
{
    char player;
    do
    {
       cout <<'\t';
        cin >> player;
        

    } while (player != 'r' && player != 'p' && player != 's' && player != 'q' );
    return player;
}
char gcc()
{
    srand(time(NULL));
    int num = rand() % 3 + 1;
    switch (num)
    {
    case 1:
        return 'r';
    case 2:
        return 'p';
    case 3:
        return 's';
    }

    return 0;
}

void sc(char choice)
{
    switch (choice)
    {
    case 'r':
        cout << "rock" << endl;
        break;
    case 'p':
        cout << "paper" << endl;
        break;
    case 's':
        cout << "scissors" << endl;
        break;
    }
}

void cw(char player, char computer)
{
    switch (player)
    {
    case 'r':
        if (computer == 'r')
            cout << "*****draw*****" << endl;
        else if (computer == 's')
            cout << "*****you won*****" << endl;
        else
            cout << "*****you lost*****" << endl;
        break;
    case 's':
        if (computer == 's')
            cout << "*****draw*****" << endl;
        else if (computer == 'r')
            cout << "*****you lost*****" << endl;
        else
            cout << "*****you won*****" << endl;
        break;
    case 'p':
        if (computer == 'p')
            cout << "*****draw*****" << endl;
        else if (computer == 's')
            cout << "*****you lost*****" << endl;
        else
            cout << "*****you won*****" << endl;
        break;
    }
}