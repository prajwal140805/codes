#include <iostream>
using namespace std;
 
void drawboard(char *spaces);
void playermove(char *spaces, char player);
void computermove(char *spaces, char computer);
bool checkwin(char *spaces, char player, char computer);
bool checktie(char *spaces);

int main()
{
    char spaces[9] = {' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '};
    char player = 'X';
    char computer = 'O';
    bool running = true;

    drawboard(spaces);
    while (running)
    {
        playermove(spaces, player);
        drawboard(spaces);
        if (checkwin(spaces, player, computer))
        {
            running = false;
            break;
        }
        computermove(spaces, computer);
        drawboard(spaces);
        if (checkwin(spaces, player, computer))
        {
            running = false;
            break;
        }

        else if (checktie(spaces))
        {
            running = false;
            break;
        }
    }
    cout << "THANKS FOR PLAYING!\n";

    return 0;
}
void drawboard(char *spaces)
{
    cout << "     |     |     " << '\n';
    cout << "  " << spaces[0] << "  |  " << spaces[1] << "  |  " << spaces[2] << '\n';
    cout << "_____|_____|_____" << '\n';
    cout << "     |     |     " << '\n';
    cout << "  " << spaces[3] << "  |  " << spaces[4] << "  |  " << spaces[5] << '\n';
    cout << "_____|_____|_____" << '\n';
    cout << "     |     |     " << '\n';
    cout << "  " << spaces[6] << "  |  " << spaces[7] << "  |  " << spaces[8] << '\n';
    cout << "     |     |     " << '\n';
}
void playermove(char *spaces, char player)
{
    int number;
    do
    {
        cout << "Enter the spot to place the marker (1-9): ";
        cin >> number;
        number--;
        if (spaces[number] == ' ')
        {
            spaces[number] = player;
            break;
        }
    } while (number < 0 || number > 8 || spaces[number] != ' ');
}

void computermove(char *spaces, char computer)
{
     cout << "\n";
    char player = (computer == 'X') ? 'O' : 'X';
    for (int i = 0; i < 9; i++)
    {
        if (spaces[i] == ' ')
        {
            spaces[i] = computer;
            if (checkwin(spaces, player , computer))
                return;
            spaces[i] = ' ';  
        }
    }

     
    
    for (int i = 0; i < 9; i++)
    {
        if (spaces[i] == ' ')
        {
            spaces[i] = player;
            if (checkwin(spaces, player,computer))
            {
                spaces[i] = computer;
                return;
            }
            spaces[i] = ' ';  
        }
    }

     
    if (spaces[4] == ' ')
    {
        spaces[4] = computer;
        return;
    }

    // Step 4: Take a corner if available
    int corners[] = {0, 2, 6, 8};
    for (int i : corners)
    {
        if (spaces[i] == ' ')
        {
            spaces[i] = computer;
            return;
        }
    }

    // Step 5: Take a side
    int sides[] = {1, 3, 5, 7};
    for (int i : sides)
    {
        if (spaces[i] == ' ')
        {
            spaces[i] = computer;
            return;
        }
    }
}

bool checkwin(char *spaces, char player, char computer)
{
    if ((spaces[0] != ' ') && (spaces[0] == spaces[1]) && (spaces[1] == spaces[2]))
    {
        spaces[0] == player ? cout << "YOU WON!\n" : cout << "YOU LOST!\n";
    }
    else if ((spaces[3] != ' ') && (spaces[3] == spaces[4]) && (spaces[4] == spaces[5]))
    {
        spaces[3] == player ? cout << "YOU WON!\n" : cout << "YOU LOST!\n";
    }
    else if ((spaces[6] != ' ') && (spaces[6] == spaces[7]) && (spaces[7] == spaces[8]))
    {
        spaces[6] == player ? cout << "YOU WON!\n" : cout << "YOU LOST!\n";
    }
    else if ((spaces[0] != ' ') && (spaces[0] == spaces[3]) && (spaces[3] == spaces[6]))
    {
        spaces[0] == player ? cout << "YOU WON!\n" : cout << "YOU LOST!\n";
    }
    else if ((spaces[1] != ' ') && (spaces[1] == spaces[4]) && (spaces[4] == spaces[7]))
    {
        spaces[1] == player ? cout << "YOU WON!\n" : cout << "YOU LOST!\n";
    }
    else if ((spaces[2] != ' ') && (spaces[2] == spaces[5]) && (spaces[5] == spaces[8]))
    {
        spaces[2] == player ? cout << "YOU WON!\n" : cout << "YOU LOST!\n";
    }
    else if ((spaces[0] != ' ') && (spaces[0] == spaces[4]) && (spaces[4] == spaces[8]))
    {
        spaces[0] == player ? cout << "YOU WON!\n" : cout << "YOU LOST!\n";
    }
    else if ((spaces[6] != ' ') && (spaces[6] == spaces[4]) && (spaces[4] == spaces[2]))
    {
        spaces[6] == player ? cout << "YOU WON!\n" : cout << "YOU LOST!\n";
    }
    else
    {
        return false;
    }
    return true;
}
bool checktie(char *spaces)
{

    for (int i = 0; i < 9; i++)
    {
        if (spaces[i] == ' ')
        {
            return false;
        }
    }
    cout << "DRAW!\n";
    return true;
}