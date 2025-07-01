#include <iostream>
#include <iomanip>
 using namespace std;
 class circle{
 private:
 double radius;
 const double pi = 3.1415;
 public:  
circle(){  
    radius = 0;  
}  
void setradius(  ){ 
    double r;
    cout << "Enter the radius of circle: ";
    cin >> r;
    cout ;
        cout << "m";

    cin>>r;
    if(r>=0){  
        radius = r;  
    }  
    else{  
        cout<<"Invilad Radius!";  
    }  
}  
double CalculateArea() {  
    return pi*radius*radius;  
}  
void DisplayCircle() {  
    cout<<"Radius : " << radius <<endl;  
    cout<<"Area : " << CalculateArea() <<endl;  
}
 };
 int main() {
 circle c1;
 c1.setradius();
 c1.CalculateArea();
 c1.DisplayCircle();
 return 0;
 }