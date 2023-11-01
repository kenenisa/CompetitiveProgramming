class Solution {
public:

    int openLock(vector<string>& deadends, string target) {
        int t = stoi(target);
        bool visited[10000]{};
        for(string dead : deadends){
            visited[stoi(dead)] = true;
        }
        if(visited[0])
            return -1;
        visited[0] = true;
        deque<pair<short,short>> q;
        q.push_back(make_pair(0,0));
        while(!q.empty()){
            pair<short,short> node = q.front();
            q.pop_front();
            if(node.first == t)
                return node.second;
            for(short i = 0;  i < 4;i++){
                short exp = pow(10,i);
                short inc = node.first;
                short dec = node.first;
                short place = floor((node.first % (short)pow(10,i+1))/(short)pow(10,i));
                if(place == 9)
                    inc -= exp * 9;
                else
                    inc += exp;
                
                if(place == 0)
                    dec += (exp * 9);
                else
                    dec -= exp;
                
                if(!visited[inc]){
                    q.push_back(make_pair(inc,node.second+1));
                    visited[inc] = true;
                }
                if(!visited[dec]){
                    q.push_back(make_pair(dec,node.second+1));
                    visited[dec]= true;
                }
            }

        }
        return -1;
    }
};

// class Solution:
//     def openLock(self, deadends: List[str], target: str) -> int:
        
//         def dial(s,i):
//             a = s[:i]
//             b = s[i+1:]
//             return [a+str((int(s[i])+1)%10)+b,a+str((int(s[i])-1)%10)+b]
        
//         visited = set(deadends)
//         if '0000' in visited:
//             return -1
//         visited.add('0000')
//         q = deque([('0000',0)])
//         while q:
//             node,d = q.popleft()
//             if node == target:
//                 return d
//             for i in range(4):
//                 inc,dec = dial(node,i)
//                 if inc not in visited:
//                     q.append((inc,d+1))
//                     visited.add(inc)
//                 if dec not in visited:
//                     q.append((dec,d+1))
//                     visited.add(dec)
//         return -1
                
