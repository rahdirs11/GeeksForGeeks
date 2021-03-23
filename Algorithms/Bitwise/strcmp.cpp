#include <iostream>
using namespace std;

int strcmp(string str1, string str2) {
    int i;
    for (i = 0; str1[i] & str2[i]; ++i) {
        if (str1[i] == str2[i] || (str1[i] ^ 32) == str2[i]) {
            continue;
        } else {
            break;
        }
    }

    if (str1[i] == str2[i]) {
        return 0;
    }
    if (str2[i] | 32 > str1[i] | 32) {
        return -1;
    }
    return 1;
}


int main() {
    string str1, str2;
    cin >> str1 >> str2;

    cout << strcmp(str1, str2) << endl;
    return 0;
}