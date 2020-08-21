#include <iostream>

using namespace std;

long long modpow(long long a, long long n, long long mod = 1000000007) {
    long long res = 1;
    while (n > 0) {
        a %= mod;
        if (n & 1) {
            res = (res * a) % mod;
        }
        a = (a * a) % mod;
        n >>= 1;
    }
    return (res + mod) % mod;
}

/*
int main() {
    cout << modpow(2, 3) << endl;
    cout << modpow(2, 64) << endl;
    cout << modpow(3, 100938485, 10) << endl;
}
*/