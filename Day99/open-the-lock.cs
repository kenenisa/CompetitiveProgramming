class Solution {
public:
    pair<short,short> dial(short num,short i){
        short exp = pow(10,i);
        short inc = num;
        short dec = num;
        short place = floor((num % (short)pow(10,i+1))/(short)pow(10,i));
        if(place == 9)
            inc -= exp * 9;
        else
            inc += exp;
        
        if(place == 0)
            dec += (exp * 9);
        else
            dec -= exp;
        
        return make_pair(inc,dec);
    }
    int openLock(vector<string>& deadends, string target) {
        int t = stoi(target);
        unordered_set<short> visited;
        
        for(string dead : deadends){
            visited.insert((short) stoi(dead));
        }
        if(visited.find(0) != visited.end())
            return -1;
        visited.insert(0);
        deque<pair<short,short>> q;
        q.push_back(make_pair(0,0));
        while(!q.empty()){
            pair<short,short> node = q.front();
            q.pop_front();
            if(node.first == t)
                return node.second;
            for(short i = 0;  i < 4;i++){
                pair<short,short> mod = dial(node.first,i);
                if(visited.find(mod.first) == visited.end()){
                    q.push_back(make_pair(mod.first,node.second+1));
                    visited.insert(mod.first);
                }
                if(visited.find(mod.second) == visited.end()){
                    q.push_back(make_pair(mod.second,node.second+1));
                    visited.insert(mod.second);
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
                
