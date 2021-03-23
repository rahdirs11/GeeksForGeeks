#include <iostream>
using namespace std;

/**
 * Find xor of two numbers without using ^ operator
 * 
 * 
 * We can traverse through each bit and check if they are equal, if yes, then xor will be zero, else itll be the or of the two bits
 * 
 * */



int main() {
    int a{}, b{};
    cin >> a >> b;
    int result{}, Xor{};
    // assuming the numbers are 4 bytes in size;
    for (int i = 31; i >= 0; --i) {
        bool x = a & (1 << i), y = b & (1 << i);
        if (x & y) {
            Xor = 0;
        } else {
            Xor = x | y;
        }
        result <<= 1;
        result |= Xor;
    }
    cout << result << endl;
    return 0;
}