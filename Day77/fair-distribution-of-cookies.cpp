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
                distribution[j] += cook[i];
                dfs(i+1,distribution);
                distribution[j] -= cook[i];
            }
        }
    }
    int distributeCookies(vector<int>& cookies, int kk) {
        n = cookies.size();
        if (n == k){
            return *max_element(cookies.begin(),cookies.end());
        }else{
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

    }
};
// Python TOO SLOW
// class Solution:
//     def distributeCookies(self, cookies: List[int], k: int) -> int:
//         n = len(cookies)
//         if n == k:
//             return max(cookies)
//         result = float('inf')
//         def dfs(i,distribution):
//             nonlocal result
//             if i >= n:
//                 result = min(result,max(distribution))
//                 return
//             for j in range(k):
//                 distribution[j] += cookies[i]
//                 dfs(i+1,distribution)
//                 distribution[j] -= cookies[i]
//         dfs(0,[0]*k)
//         return result