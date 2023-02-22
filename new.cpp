#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<queue>
using namespace std;
char a[50010];
int b[30];
int main() {
     while(scanf("%s",a)!=EOF) {
         int n=strlen(a),flag1,flag2=0;
         if (n<26) {
             printf("-1\n");
             continue;
         }
         for (int i=0 ; i<n-25 ; i++ ) {
             flag1=1;
             memset(b,0,sizeof(b));
             for (int j=i ; j<i+26 ; j++) {
                 if (a[j]>='A' && a[j]<='Z') {
                     b[a[j]-'A']++;
                 }
                 if  (b[a[j]-'A']>=2) {
                     flag1=0;
                     break;
                 }
             }
             if (!flag1) continue;
             flag2=1;
             for (int j=i ; j<i+26 ; j++) {
                 if (a[j]=='?') {
                     for (int k=0 ; k<26 ; k++) {
                         if (b[k]==0) {
                             a[j]=k+'A';
                             b[k]=1;
                             break;
                         }
                     }
                 }
             }
             if (flag2) break;
         }
         if (flag2) {
             for (int i=0 ;i<n ;i++){
                 if (a[i]=='?') printf("A");
                 else printf("%c",a[i]);
             }
             printf("\n");
         }else printf("-1\n");
     }
     return 0;
 }

//  #include <bits/stdc++.h>

using namespace std;

const int N = 2e3 + 5;
int a[N];

int main(){
    int n;
    scanf("%d", &n);
    for(int i = 0; i < n; ++i){
        scanf("%d", &a[i]);
    }

    int ans = n - 1;
    map<int, int> freq; 
    for(int i = 0; i < n; ++i){
        bool validPrefix = true;
        for(int j = 0; j < i; ++j){
            freq[a[j]]++;
            if(freq[a[j]] == 2){
                validPrefix = false;
                break;
            }
        }
        int min_index_suffix = n;
        for(int j = n - 1; j >= i; --j){
            freq[a[j]]++;
            if(freq[a[j]] == 1){
                min_index_suffix = j;
            }
            else break;
        }
        if(validPrefix){
            ans = min(ans, min_index_suffix - i);
        }
        
        freq.clear();
    }
    cout << ans << '\n';
}