 #include <iostream>
 using namespace std;
 inline double cylinderVolume(double radius, double height) {
 cout<<"The volume is :" << 3.14159 * radius * radius * height;
 }
 int main() {
 double  radius, height;
 cout << "Enter the radius of the cylinder: ";  
cin >> radius;  
cout << "Enter the height of the cylinder: ";  
cin >> height;  
  
cylinderVolume(radius, height);  
  
return 0;
 }