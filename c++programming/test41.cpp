#include <iostream>
#include <string>  // for getline
#include <sstream> // for stringstream
using namespace std;

// Function with default argument for rate
float simpleInterest(float principal, float time, float rate = 5.0)
{
    return (principal * time * rate) / 100;
}

int main()
{
    float principal, time, rate;
    string rateInput;

    cout << "Enter principal and time: ";
    cin >> principal >> time ;
    cin.ignore();
    getline(cin, rateInput); // Accept full line including empty

    if (rateInput.empty())
    {
        // User pressed enter without typing a rate
        cout << "Simple Interest (default 5%) = " << simpleInterest(principal, time) << endl;
    }
    else
    {
        stringstream(rateInput) >> rate; // Convert input string to float
        cout << "Simple Interest (" << rate << "%) = " << simpleInterest(principal, time, rate) << endl;
    }


    return 0;
}
