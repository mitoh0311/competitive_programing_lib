#include <iostream>
#include <vector>

using namespace std;

// 半開区間[begin, end)内の自然数をstrideおきに列挙してvectorで出力
template<typename T> vector<T> range(T begin, T end, T stride = 1) {
    vector<T> vec;
    for (T i = begin; i < end; i += stride) {
        vec.push_back(i);
    }
    return vec;
}