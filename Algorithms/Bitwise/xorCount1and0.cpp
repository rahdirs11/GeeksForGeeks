#include <iostream>
using namespace std;

int main() {
    int n{};
    cin >> n;
    int count1{}, count0{};
    while (n) {
        int y = n ^ 1;
        if (y) {
            ++count0;
        } else {
            ++count1;
        }
        n >>= 1;
    }
    cout << (count1 ^ count0) << endl;
    return 0;
}