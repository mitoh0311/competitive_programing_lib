#include <iostream>

using namespace std;

template<typename T> T mod_factorial(T in, T mod = 1000000007) {
    long long ans = 1;
    for (int i=2; i < in + 1; ++i) {
        ans *= i;
        ans %= mod;
    }
    return ans;
}