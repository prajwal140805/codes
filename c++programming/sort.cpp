#include <iostream>
using namespace std;

void sort(int array[], int size);

int main()
{
    int n;
    cout << "Enter the size of the array: ";
    cin >> n;

    int* array = new int[n]; 

    cout << "Enter the elements of the array: ";
    for (int i = 0; i < n; i++) {
        cin >> array[i];
    }

    cout << "The elements of the array are:------- ";
    for (int i = 0; i < n; i++) {
        cout << array[i] << " ";
    }

    cout << endl;
    sort(array, n);

    cout << "The sorted elements of the array are: ";
    for (int i = 0; i < n; i++) {
        cout << array[i] << " ";
    }

    delete[] array; 
    return 0;
}

void sort(int array[], int size)
{
    for (int i = 0; i < size - 1; i++) {
        for (int j = 0; j < size - i - 1; j++) {
            if (array[j] > array[j + 1]) {
                swap(array[j], array[j + 1]);
            }
        }
    }
}