#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int n, four, three, two, one, result=0;
    cin >> n;
    vector<int> s(n);

    for (int i = 0; i < n; i++) {
        cin >> s[i];
    }
    sort(s.rbegin(), s.rend());
    int left = 0, right = n - 1;
    while (left <= right) {
        int count = s[left];
        while (left < right and count + s[right] <= 4) {
            count += s[right];
            right--;
        }
        result++;
        left++;
    }
    cout << result << "\n";
}