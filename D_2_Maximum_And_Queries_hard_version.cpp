#include <iostream>
#include <vector>

typedef long long LL;
using namespace std;

LL incur(LL v, LL mask)
{
    return (v + mask) / mask * mask;
}

int main()
{
    LL n, q;
    cin >> n >> q;

    vector<LL> a(n);
    for (LL i = 0; i < n; ++i) {
        cin >> a[i];
    }

    for (LL qq = 0; qq < q; ++qq) {
        LL k;
        cin >> k;
        vector<LL> b;
        for (auto x : a) {
            b.push_back(x);
        }
        LL result = 0;

        for (LL i = 60; i >= 0; --i) {
            LL s = 0;
            vector<LL> save;
            for (auto x : b) {
                save.push_back(x);
            }

            for (LL j = 0; j < n; ++j) {
                if ((b[j] & (1 << i)) == 0) {
                    s -= b[j];
                    b[j] = incur(b[j], 1 << i);
                    s += b[j];

                    if (s > k)
                        break;
                }
            }

            if (s > k) {
                b = new vector<LL>();
                for (auto x : save) {
                    b.push_back(x);
                }
            } else {
                k -= s;
                result += (1 << i);
            }
        }

        cout << result << endl;
    }

    return 0;
}
