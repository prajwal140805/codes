#include <iostream> 
#include <stdexcept>  
using namespace std; 
float Division(float num, float den) 
{  
if (den == 0)  
{ 
throw den; 
} 
return (num / den); 
} 
int main() 
{ 
float numerator, denominator, result;  
numerator = 12.5; 
denominator = 0; 
try  
{ 
result = Division(numerator, denominator); 
cout << "The quotient is "<< result << endl; 
} 

catch (float e)  
{ 
cout << "Exception occurred" << endl << "Math error: Attempted to divide by zero."; 
} 
}