#include<iostream>
#include<vector>

using namespace std;
int n,m,u,v;
vector<vector<int> > df(1<<18);
vector<int> edges;
vector<int> color(1<<18,0);

bool dfs(int i){
    for(int k = 0; k < df[i].size();k++){
        int j = df[i][k];
        if (color[i] == color[j])
            return false;
        if (color[j] == 0){
            if(color[i] == 2){
                color[j] = 1;
            }else{
                color[j] = 2;
            }
            if(!dfs(j))
                return false;
        }
    }
    return true;
}

int main () {
    cin >> n >> m;
    color[1] = 1;
    for(int i = 0; i < m;i++){
        cin >> u >> v;
        df[u].push_back(v);
        df[v].push_back(u);
        edges.push_back(u);
    }
    if(dfs(1)){
        cout << "YES" << endl;
        for(int i = 0; i < m; i++){
            if (color[edges[i]] == 1){
                cout << "1";
            }else{
                cout << "0";
            }
        }
        cout << endl;
    }else{
        cout << "NO" << endl;
    }
    


    return 0;
}