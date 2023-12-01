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

    int t = read<int>();
    while (t--) {
        int n = read<int>();
        vector<int> a = readVector<int>(n);
        if (n == 1) {
            cout << 0 << "\n";
            continue;
        }
        int mx = 0;

        for (int i = 0; i < n; i++) {
            mx = max(mx, a[i]);
        }

        vector<int> result;
        while (mx) {
            int valid = 1;
            for (int i = 1; i < n; i++) {
                if (a[i] != a[i - 1]) {
                    valid = 0;
                }
            }
            if (valid) {
                break;
            }
            int ind = (mx % 2 == 0);
            for (int i = 0; i < n; i++) {
                a[i] = (a[i] + ind) / 2;
            }
            mx = (mx + ind) / 2;
            result.push_back(ind);
        }

        cout << (int)result.size() << "\n";
        if (result.size() <= n) {
            for (auto it : result) {
                cout << it << " ";
            }
        }
        if (result.size() != 0)
            cout << "\n";

        // int mx = a[0];
        // int mi = a[0];
        // bool valid = true;
        // for(int i = 0; i < n;i++){
        //     mx = max(mx,a[i]);
        //     mi = min(mi,a[i]);
        //     if(valid && a[0] != a[i]) valid = false;
        // }
        // if (valid){
        //     cout << 0 << "\n";
        //     continue;
        // }
        // long long operations = 0;
        // vector<int> chosen_x;
        // while(mx != mi){

        //     int x = mx - mi;
        //     int maxx = -1;
        //     int minn = int(1e9)+1;
        //     for(int i = 0; i < n;i++){
        //         a[i] = (a[i] + x) / 2;
        //         maxx = max(maxx,a[i]);
        //         minn = min(minn,a[i]);
        //     }
        //     mx = maxx;
        //     mi = minn;
        //     operations += 1;
        //     if (operations <= n) chosen_x.push_back(x);
        // }
        // cout << operations << "\n";

        // if (operations <= n){
        //     for(int i = 0; i < chosen_x.size();i++){
        //         cout << chosen_x[i];
        //         if(i != chosen_x.size()-1){
        //             cout << " ";
        //         }
        //     }
        //     cout << "\n";
        // }
    }

    return 0;
}
