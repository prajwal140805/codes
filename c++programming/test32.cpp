 #include<iostream>
 #include<cmath>
 using namespace std;
 double CalculateDistance(int x1, int y1,int x2=1 , int y2=1 ){
 cout<<"Distance = " << sqrt((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1))<<endl;
 }
 int main() {
 double x1,y1,x2,y2;
 cout<<"Enter x1 y1 :";
 cin>> x1 >> y1 ;
 CalculateDistance(x1,y1);  
  
return 0;
 }
 