#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int main()
{
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) {

        ll n, b, c, d;
        cin >> n >> b >> c >> d;
        ll rac = (n - n % 7) / 7 + 1;
        rac -= (n % 7 == 0 ? 1 : 0);
        ll lef = 1, rig = rac;
        ll ans = rac;
        while (lef <= rig) {
            ll mid = (lef + rig) / 2;
            if (b <= (mid + 1) / 2 * c + d * mid) {
                ans = mid;
                rig = mid - 1;
            } else {
                lef = mid + 1;
            }
        }
        long long rac2 = (ans + 1) / 2;
        long long taodeptrai = rac2 * c + d * ans;
        b = b - taodeptrai;
        ll tmp = rac2;
        b = max(b, 0LL);
        tmp = tmp + (b / c);
        tmp = tmp + (b % c != 0);
        cout << n - tmp << "\n";
    }
}