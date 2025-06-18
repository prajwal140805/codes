#include <iostream>  
#include <stdexcept> 
using namespace std;  
int main() 
{ 
int a[10],i,size;  
try 
{ 
cout<<"Enter array size:"<<endl;
cin>>size; 
if (size>10) throw 5; 
if (size<=0) throw 3.2; 
cout<<"Enter array elements"<<endl; 
for (i=0;i<size;i++)  
cin>>a[i]; 
cout<<"Array elements are:"<< endl; 
for (i=0;i<size;i++)  
cout<<a[i]<<"\t"; 
} 
 

catch (int x)  
{ 
cout<<"Array size out of bounds exception occured"<<endl; 
} 
catch (double y) 
{ 
cout<<"Neagative array size exception occured"<<endl; 
} 
return 0; 
} 