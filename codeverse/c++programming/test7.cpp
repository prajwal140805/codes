#include <iostream>
using namespace std;
int main()
{

   string questions[] = {"1. India belongs to which continent?",
                         "2. When india got independence?",
                         "3. Is the earth flat?",
                         "4. where is golgumbuz?"};
   string options[][4] = {{"A. asia","B. africa","C. america","D. antartica",},
                          {"A. 1964", "B. 1949", "C. 1947", "D. 1957"},
                          {"A. yes", "B. no", "C. its cubical", "D. don't know"},
                          {"A. delhi", "B. mumbai", "C. bidar", "D. bijapur"}};
   char answerkey[] = {'A', 'C', 'B', 'D'};
   int size = sizeof(questions) / sizeof(questions[0]);
   char guess;
   int score;
   for (int i = 0; i < size; i++)
   {
      cout << "****************************************\n";
      cout << questions[i] << '\n';
      cout << "****************************************\n";
      for (int j = 0; j < sizeof(options)[i] / sizeof(options[i][0]); j++)
      {
         cout << options[i][j] << '\n';
      }
      cin >> guess;
      guess = toupper(guess);
      if (guess == answerkey[i])
      {
         cout << "CORRECT\n";
         score++;
      }
      else
      {
         cout << "WRONG\n"; 
         cout << "Answer: " << answerkey[i] << '\n';                   
      }
   }
   cout << "****************************************\n";
   cout << "*************RESULTS********************'\n'";
   cout << "****************************************\n";
    cout << "CORRECT GUESSES: " << score << '\n';
    cout << "NUMBER OF QUESTIONS: " << size << '\n';
    cout << "PERCENTAGE: " << (score * 100) /(double)size << "%\n";

   return 0;
}
