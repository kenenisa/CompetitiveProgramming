#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

typedef long long LL;

bool sortcol(vector<int>& v1, vector<int>& v2)
{
    return v1[0] < v2[0];
}

int main()
{
    int n, m;
    cin >> n >> m;
    vector<int> a;
    for (int i = 0; i < n; i++) {
        LL x;
        cin >> x;
        a.push_back(x);
    }
    int q[m][2];
    int dist[n + 1];
    std::fill_n(dist, n + 1, 0);
    for (int i = 0; i < m; i++) {
        cin >> q[i][0] >> q[i][1];
        dist[q[i][0]-1] += 1;
        dist[q[i][1]] -= 1;
    }

    vector< vector<int> > d;
    vector<int> v;
    v.push_back(dist[0]);
    v.push_back(0);
    d.push_back(v);

    for (int i = 1; i < n; i++) {
        dist[i] += dist[i - 1];
        vector<int> v;
        v.push_back(dist[i]);
        v.push_back(i);
        d.push_back(v);
    }
    sort(d.begin(), d.end(), sortcol);
    reverse(d.begin(), d.end());
    sort(a.begin(), a.end());
    reverse(a.begin(), a.end());

    int final[n];
    std::fill_n(final, n, 0);

    for (int i = 0; i < n; i++) {
        final[d[i][1]] = a[i];
    }
    vector<LL> prefixSum;
    prefixSum.push_back(0);

    for (int i = 0; i < n; i++) {
        prefixSum.push_back(*prefixSum.rbegin() + final[i]);
    }
    LL result = 0;
    for (int j = 0; j < m; j++) {
        result += prefixSum[q[j][1]] - prefixSum[q[j][0] - 1];
    }
    cout << result << endl;

    return 0;
}