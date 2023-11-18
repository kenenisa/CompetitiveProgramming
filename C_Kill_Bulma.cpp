#include <iostream>
#include <string>
#include <vector>

using namespace std;

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
    const int n = read<int>();

    int arr[n][n];
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            cin >> arr[i][j];
        }
    }
    vector<vector<int> > prefixSum(n, vector<int>(n, 0));
    // int prefixSum[n][n] = {{0}};

    for (int j = 0; j < n; ++j) {
        prefixSum[0][j] = arr[0][j];
        if (j > 0) {
            prefixSum[0][j] += prefixSum[0][j - 1];
        }
    }
    for (int i = 0; i < n; ++i) {
        prefixSum[i][0] = arr[i][0];
        if (i > 0) {
            prefixSum[i][0] += prefixSum[i - 1][0];
        }
    }
    for (int i = 1; i < n; ++i) {
        for (int j = 1; j < n; ++j) {
            prefixSum[i][j] = arr[i][j] + prefixSum[i - 1][j] + prefixSum[i][j - 1] - prefixSum[i - 1][j - 1];
        }
    }
    int x1, y1, x2, y2, q;
    long long bluma;
    cin >> q;
    long long sum = 0;
    for (int i = 0; i < q; i++) {
        cin >> x1 >> y1 >> x2 >> y2;
        if (x2 < x1) {
            swap(x2, x1);
        }
        if (y2 < y1) {
            swap(y2, y1);
        }

        sum += prefixSum[x2][y2];

        if (x1 > 0) {
            sum -= prefixSum[x1 - 1][y2];
        }

        if (y1 > 0) {
            sum -= prefixSum[x2][y1 - 1];
        }

        if (x1 > 0 && y1 > 0) {
            sum += prefixSum[x1 - 1][y1 - 1];
        }
    }
    cin >> bluma;
    if (sum*2 > bluma) {
        cout << "YES"
             << "\n";
    } else {
        cout << "NO"
             << "\n";
    }
    return 0;
}