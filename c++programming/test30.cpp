#include<iostream>
 using namespace std;
 class DetermineTriangles{
 private:
 float side1;
 float side2;
 float side3;
 public:  
DetermineTriangles(float s1, float s2, float s3){  
    side1 = s1;  
    side2 = s2;  
    side3 = s3;  
}  
void Determine() {  
    if(side1 == side2 && side2 == side3){  
        cout<<"it's an equilateral triangle"<<endl;  
    }  
      
    else if(side1 == side2 || side2 == side3 || side1 == side3) {  
        cout<<"it's an isosceles triangle"<<endl;  
    }  
    else{  
        cout<<"it's a scalene triangle"<<endl;  
    }  
}
 };

 int main() {
 double side1, side2, side3;
 cout << "Enter the length of side 1: ";  
cin >> side1;  
cout << "Enter the length of side 2: ";  
cin >> side2;  
cout << "Enter the length of side 3: ";  
cin >> side3;  
DetermineTriangles t1(side1, side2, side3);  
t1.Determine();  
return 0;
 }