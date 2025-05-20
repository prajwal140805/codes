 #include <iostream>
 using namespace std;
 double DiscountedPrice(double price = 100, double discount = 10) {
 cout<<"Final Price : " << price - (price * discount / 100);
 }
 int main() {
 double price, discount;
 cout << "Enter price (or press Enter to use default 100): ";
 cin >> price;
 cout << "Enter discount (or press Enter to use default 10%): ";
 cin >> discount;
 DiscountedPrice(price, discount);  
return 0;
 }