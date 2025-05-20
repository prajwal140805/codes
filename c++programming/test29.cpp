#include<iostream>
 using namespace std;
 class BankAccount{
 private:
 int AccountNumber;
 string AccountHolderName;
 double Balance;
 public:  
BankAccount(int accnum, string name, double balance){  
    AccountNumber = accnum;  
    AccountHolderName = name;  
    Balance = balance;  
    }  
    void DepositeMoney() {  
        float Deposite = 500;  
        Balance = Balance + 500;  
    }  
    void WithdrawMoney(){  
        float Withdraw = 1500;  
        Balance = Balance - 1500;  
    }  
    void AccountDetails() {  
        cout<<"AccountNumber :" << AccountNumber <<endl;  
        cout<<"AccountHolderName :" << AccountHolderName <<endl;  
        cout<<"Balance :" << Balance <<endl;  
    }
 };
 int main() {
 BankAccount b1(101,"Navnit Nayan",50000);
 b1.DepositeMoney();
 b1.WithdrawMoney();
 b1.AccountDetails();
 return 0;
 }