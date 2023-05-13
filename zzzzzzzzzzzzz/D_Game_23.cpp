#include <algorithm>
#include <iostream>

using namespace std;
typedef long long LL;

LL n, m;

int recur(LL val, int move, int count)
{
    if (val == m) {
        return count;
    }
    val *= move;
    if (val > m) {
        return -1;
    }
    return std::max(recur(val, 2, count + 1), recur(val, 3, count + 1));
}

int main()
{
    cin >> n >> m;
    cout << std::max(recur(n, 2, 0), recur(n, 3, 0)) << endl;
    return 0;
}