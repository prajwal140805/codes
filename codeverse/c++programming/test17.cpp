#include <iostream>
#include <vector>
using namespace std;

class Product
{
public:
    int id;
    string name;
    double price;

    Product(int i, string n, double p) : id(i), name(n), price(p) {}
};

class Cart
{
    vector<Product> products;

public:
    void addProduct(const Product &product)
    {
        products.push_back(product);
        cout << product.name << " added to the cart." << endl;
    }

    void removeProduct(int id)
    {
        for (auto it = products.begin(); it != products.end(); ++it)
        {
            if (it->id == id)
            {
                cout << it->name << " removed from the cart." << endl;
                products.erase(it);
                return;
            }
        }
        cout << "Product not found in the cart." << endl;
    }

    void displayCart()
    {
        cout << "Cart contents:" << endl;
        for (const auto &product : products)
        {
            cout << "ID: " << product.id << ", Name: " << product.name << ", Price: $" << product.price << endl;
        }
    }
};

int main()
{
    Cart cart;
    Product p1(1, "Laptop", 1000), p2(2, "Phone", 500), p3(3, "Headphones", 100);

    cart.addProduct(p1);
    cart.addProduct(p2);
    cart.displayCart();

    cart.removeProduct(2);
    cart.displayCart();

    return 0;
}