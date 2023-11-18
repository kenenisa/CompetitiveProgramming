#include <iostream>
#include <vector>
#include <string>
#include <set>
using namespace std;

// Function to read a single value of type T
template <typename T>
T read() {
    T x;
    cin >> x;
    return x;
}

// Function to read a vector of type T
template <typename T>
vector<T> readVector(int n) {
    vector<T> v(n);
    for (int i = 0; i < n; ++i) {
        v[i] = read<T>();
    }
    return v;
}

// Function to read a string
string readString() {
    string s;
    cin >> s;
    return s;
}

// Function to read a line of string
string readLine() {
    string s;
    getline(cin, s);
    return s;
}

int main() {
    // Example usage:
    //int n = read<int>(),
    //vector<int> v = readVector<int>(n),
    //string s = readString(),
    //string line = readLine();

    int t = read<int>();
    while(t--){
        int n = read<int>();
        vector<int> a = readVector<int>(n);
        set<int> st(a.begin(), a.end());
        cout << st.size() << "\n";
    }

    return 0;
}