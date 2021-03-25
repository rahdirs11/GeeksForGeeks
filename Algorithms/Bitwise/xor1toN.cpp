#include <iostream>
using namespace std;

int xor1toN(int n) {
    if (n % 4 == 0) {
        return 0;
    } else if (n % 4 == 1) {
        return 1;
    } else if (n % 4 == 2) {
        return n + 1;
    } else {
        return 0;
    }
}


int main() {
    int n{};
    cin >> n;
    cout << xor1toN(n) << endl;
}