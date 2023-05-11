#include<iostream>
using namespace std;
// i dont understand this
long  long n, l, r, s = 1, ans;
void solve(long  long x, long  long b, long  long l, long  long r, long  long d)
{ 
    if (x > b || l > r)
        return;
    else
    {
        long  long middle = (x + b) / 2;
        if (r < middle)
            solve(x, middle - 1, l, r, d / 2);
        else if (middle < l)
            solve(middle + 1, b, l, r, d / 2);
        else
        {
            ans += d % 2;
            solve(x, middle - 1, l, middle - 1, d / 2);
            solve(middle + 1, b, middle + 1, r, d / 2);
        }
    }
}
int main()
{
    cin >> n >> l >> r;
    long  long p = n;
    while (p >= 2)
    {
        p /= 2;
        s = s * 2 + 1;
    }
    solve(1, s, l, r, n);
    cout << ans << endl;
    return 0;
}