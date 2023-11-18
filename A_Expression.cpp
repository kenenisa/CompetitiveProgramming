#include<iostream>

using namespace std;

int main(){
    int a,b,c;
    cin >> a;
    cin >> b;
    cin >> c;

    cout << max(a+b+c,max((a+b)*c,max(a*(b+c),a*b*c))) << "\n";

    return 0;
}