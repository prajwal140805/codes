#include <iostream> 
using namespace std; 
void practical (int x) 
{ 
try { 
          throw 20; 
          throw 30; 
        } 
catch (int e)   {  
            cout<<" Exception caught:\n" << e<< "\n"; 
         } 
catch (int z ) 
         {  
            cout<<"Exception caught:\n" << z<< "\n"; 
         } 
} 
int main() 
{ cout << "Hello" << flush<<endl; // flushes buffer immediately

   practical (1); 
   practical (2); 
   return 0; 
}