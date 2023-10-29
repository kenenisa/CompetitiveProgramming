class Solution {
public:
    int dijkstra(int start,int n,int distanceThreshold,vector<vector<pair<int,int>>>& df){
        vector<int> distance(n,INT_MAX);
        distance[start] = 0;
        priority_queue<pair<int,int>> h;
        h.push(make_pair(0,start));
        while(!h.empty()){
            pair<int,int> node = h.top();
            h.pop();
            for(pair<int,int> item : df[node.second]){
                int i = item.second - node.first;
                if (i <= distanceThreshold && i < distance[item.first]){
                    distance[item.first] = i;
                    h.push(make_pair(-1*i,item.first));
                }
            }
        }
        int count = 0;
        for(int i: distance)
            if(i<=distanceThreshold)
                count++;
        return count;
    }
    int findTheCity(int n, vector<vector<int>>& edges, int distanceThreshold) {
        vector<vector<pair<int,int>>> df(n);
        for(auto edge:edges){
            df[edge[0]].push_back(make_pair(edge[1],edge[2]));
            df[edge[1]].push_back(make_pair(edge[0],edge[2]));
        }
        pair<int,int> rank = make_pair(INT_MAX,-1);
        for(int i = 0; i < n;i++){
            int d = dijkstra(i,n,distanceThreshold,df);
            if(rank.first >= d){
                rank = make_pair(d,i);
            }
        }
        return rank.second;
    }
};
