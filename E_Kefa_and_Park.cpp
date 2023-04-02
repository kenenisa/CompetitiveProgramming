#include<map>
#include<iostream>
#include<vector>
using namespace std;

int m;
vector<int> cats;
vector<vector<int> > tree;

int recur(int node, int path, int parent) {
    int catCount = 0, valid = 0;
    bool leaf = true;
    if(cats[node] == 0) {
        catCount = 0;
    } else {
        catCount = path + cats[node];
    }
    if(catCount > m) {
        return 0;
    }
    for(int i = 0; i < tree[node].size(); i++) {
        if(tree[node][i] == parent) {
            continue;
        }
        leaf = false;
        valid += recur(tree[node][i], catCount, node);
    }
    if(leaf) {
        return 1;
    }
    return valid;
}

int main() {
    int n,temp,x,y;
    cin >> n >> m;
    for(int i = 0; i < n; i++) {
        cin >> temp;
        cats.push_back(temp);
        tree.push_back(vector<int>());
    }
    for(int i = 0; i < n - 1; i++) {
        cin >> x >> y;
        tree[x - 1].push_back(y - 1);
        tree[y - 1].push_back(x - 1);
    }
    int result = recur(0, 0, -1);
    cout << result << endl;
    return 0;
}