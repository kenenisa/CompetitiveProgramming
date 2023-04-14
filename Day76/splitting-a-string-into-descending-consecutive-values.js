/**
 * @param {string} s
 * @return {boolean}
 */
var splitString = function(s) {
    const n = s.length
    const dfs = (i,split)=> {
        if(i>=n){
            if (split.length > 1){
                const sp = split.map(Number)
                for(let i = 1; i < sp.length; i++){
                    if(sp[i-1] != sp[i] + 1){
                        return false;
                    }
                }
                return true;
            }
            return false;
        }else{
            const m = split.slice()
            m[m.length - 1] = m[m.length - 1] + s[i]
            const l = dfs(i+1,m)
            if(l){
                return true;
            }
            split.push(s[i])
            return dfs(i+1,split.slice())
        }
    }
    return dfs(1,[s[0]])
};
// TOO SLOW
// class Solution:
//     def splitString(self, s: str) -> bool:        
//         n = len(s)
//         def dfs(i,split):
//             if i >= n:
//                 if len(split) > 1:
//                     sp = list(map(int,split))
//                     for i in range(1,len(split)):
//                         if sp[i-1] != sp[i] + 1:
//                             return False
//                     return True
//             else:
//                 mem = split[-1]
//                 split[-1] = split[-1] + s[i]
//                 l = dfs(i+1,split[::])
//                 if l:
//                     return True
//                 split[-1] = mem
//                 split.append(s[i])
//                 return dfs(i+1,split[::])
//         return dfs(1,[s[0]])
        

                