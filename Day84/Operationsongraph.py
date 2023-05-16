from collections import defaultdict
n = int(input())
t = int(input())
df = defaultdict(list)
for _ in range(t):
    a = list(map(int,input().split()))
    if len(a) > 2:
        _,u,v = a
        df[u].append(v)
        df[v].append(u)
    else:
        _,u = a
        print(*df[u])
        

# #include<iostream>
# #include<vector>
# #include <unordered_map>

# using namespace std;

# int main(){
#     unordered_map<int, vector <int> > df;
#     int n,k,m,u,v;
#     cin >> n;
#     cin >> k;
#     while(k--){
#         cin >> m;
#         if(m == 1){
#             cin >> u >> v;
#             df[u].push_back(v);
#             df[v].push_back(u);
#         }else{
#             cin >> u;
#             std::vector<int> vec = df[u];
#             for(int i = 0; i < vec.size(); i++){
#                 cout << vec[i];
#                 if(i < vec.size() - 1){
#                     cout << " ";
#                 }
#             }
#             cout << endl;

#         }
#     }
#     return 0;
# }
