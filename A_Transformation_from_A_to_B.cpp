#include<iostream>
#include<vector>


using namespace std;

bool dfs(long long a,long long b){
    cout << a << endl;
    if(a > b){
        return false;
    }
    if(a == b){
        return true;
    }
    return false || dfs(a*2,b) || dfs(10*a+1,b);

}
int main(){
    long long a, b;
    cin >> a >> b;
    if(dfs(a,b)){
        cout << "YES" << endl;
    }else{
        cout << "NO" << endl;
    }
    return 0;
}