#include <iostream>
#include <vector>
#include <limits>

using namespace std;

int main() {
    int n;
    long long p;
    cin >> n >> p;
    vector<long long> a(n);
    
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    
    int min_songs = numeric_limits<int>::max();
    int ss = -1;
    int ts = 0;
    int i = 0;
    int j = 0;
    long long mood = 0;
    
    while (i < n) {
        while (mood < p) {
            mood += a[j % n];
            j++;
            ts++;
        }
        
        if (ts < min_songs) {
            min_songs = ts;
            ss = i + 1;
        }
        
        mood -= a[i];
        i++;
        ts--;
    }
    
    cout << ss << " " << min_songs << endl;
    
    return 0;
}
