#include <iostream>

using namespace std;

int main()
{
    int n, k, l, r, t;
    cin >> t;
    while (t--) {
        cin >> n >> k;
        int left = 0, right = 0;
        while(n--){
            cin >> l >> r;
            if (l == k) {
                left++;
            }
            if (r == k) {
                right++;
            }
        }
        cout << (left >= 1 && right >= 1 ? "YES" : "NO") << "\n";
    }
    return 0;
}