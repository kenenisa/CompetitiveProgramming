
class Solution {
public:
    int result = INT_MAX;
    int n;
    int k;
    vector<int> cook;
    void dfs(int i,int* distribution){
        if(i >= n){
            int m = *max_element(distribution,distribution+k);
            result = min(result,m);
        }else{
            for(int j = 0; j < k;j++){
                int d[k];
                std::copy(distribution, distribution+k, d);
                d[j] += cook[i];
                dfs(i+1,d);
            }
        }
    }
    int distributeCookies(vector<int>& cookies, int kk) {
        n = cookies.size();
        k = kk;
        cook = cookies;
        // int dis[2] = {31,2};
        // int c[2];
        // std::copy(dis, dis+2, c);
        int distribution[k];
        std::fill_n(distribution,k,0);
        dfs(0,distribution);
        return result;
    }
};
//TOO SLOW
// class Solution:
//     def distributeCookies(self, cookies: List[int], k: int) -> int:
//         n = len(cookies)
//         result = float('inf')
//         def dfs(i,distribution):
//             nonlocal result
//             if i >= n:
//                 result = min(result,max(distribution))
//                 return
//             for j in range(k):
//                 d = distribution[::]
//                 d[j] += cookies[i]
//                 dfs(i+1,d)
//         dfs(0,[0]*k)
//         return result