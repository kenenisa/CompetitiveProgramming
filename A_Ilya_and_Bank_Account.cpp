#include <bits/stdc++.h>

using namespace std;
typedef long long LL;
// Function to read a single value of type T
template <typename T>
T read()
{
    T x;
    cin >> x;
    return x;
}

// Function to read a vector of type T
template <typename T>
vector<T> readVector(int n)
{
    vector<T> v(n);
    for (int i = 0; i < n; ++i) {
        v[i] = read<T>();
    }
    return v;
}

// Function to read a string
string readString()
{
    string s;
    cin >> s;
    return s;
}

// Function to read a line of string
string readLine()
{
    string s;
    getline(cin, s);
    return s;
}

int main()
{
    // Example usage:
    // int n = read<int>(),
    // vector<int> v = readVector<int>(n),
    // string s = readString(),
    // string line = readLine();

    int n = read<int>();
    if (n < 0) {

        int first = n % 10;
        int second = (n % 100) / 10;
        if(second < 0){
            second *= -1;
        }
        if(first < 0){
            first *= -1;
        }
        n *= -1;
        if (second > first) {
            cout << -1 * ((n/100) * 10 + first) << "\n";
        }else{
            cout << -1 * (n/10) << "\n";
        }
    } else {
        cout << n << "\n";
    }

    return 0;
}