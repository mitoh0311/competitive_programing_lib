#include <iostream>

using namespace std;

template<typename T> T factorial(T in) {
    long long ans = 1;
    for (int i=2; i < in + 1; ++i) ans *= i;
    return ans;
}