//Write a class called Circle to represent a circle. Include member variables for radius and diameter. Implement member functions to calculate the circumference #include<iostream>
 #include<iostream>
#include<string>
 using namespace std;
 class Circle{
 private:
 double radius;
 double diameter;
 const double pi = 3.14156;
 public:  
void SetCircle(double radius, double diameter){  
    this->radius=radius;  
    this->diameter=diameter;  
}  
double Circumference() {  
    return 2*pi*radius;  
}  
double Area() {  
    return pi*radius*radius;  
}  
void CircleDetails() {  
    cout<<"Radius :"<< radius <<endl;
    cout<<"Circumference :"<<Circumference()<<endl;
    cout<<"Area :"<<Area()<<endl;
}
 };
 int main () {
 Circle c1;
 c1.SetCircle(25.0,50.0);
 c1.Circumference();
 c1.Area();
 c1.CircleDetails();
 return 0;
 }