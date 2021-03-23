#include <iostream>

bool areEqual(int a, int b) {
    return a ^ b? false: true;
}

int main() {
    int a{}, b{};
    std::cin >> a >> b;
    if (areEqual(a, b)) {
        std::cout << a << " and " << b << " are equal." << std::endl;
    } else {
        std::cout << a << " and " << b << " are not equal." << std::endl;
    }
    return 0;
}