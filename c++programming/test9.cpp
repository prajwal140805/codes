#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

int main() {
    srand(time(0));
    int randomNum = rand() % 100 + 1; // Random number between 1 and 100
    int guess;
    
    cout << "Guess a number between 1 and 100: ";
    
    while (true) {
        cin >> guess;
        if (guess > randomNum) 
            cout << "Too high! Try again: ";
        else if (guess < randomNum) 
            cout << "Too low! Try again: ";
        else {
            cout << "Congratulations! You guessed it right!";
            break;
        }
    }
    
    return 0;
}
