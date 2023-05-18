class ThroneInheritance {
    unordered_map<string, vector<string> > tree;
    set<string> dead;
    string king;
public:
    ThroneInheritance(string kingName) {
        this->king = kingName;
        cout << this->king <<endl;
    }
    
    void birth(string parentName, string childName) {
        this->tree[parentName].push_back(childName);
    }
    
    void death(string name) {
        this->dead.insert(name);
    }
    void dfs(string name,vector<string> &line){
        if(this->dead.find(name) == this->dead.end()){
            line.push_back(name);
        }
        vector<string> children = this->tree[name];
        for(int i = 0;i < children.size(); i++){
            dfs(children[i],line);
        }
    }
    vector<string> getInheritanceOrder() {
        vector<string> line;
        this->dfs(this->king,line);
        return line;
    }
};

// class ThroneInheritance:

//     def __init__(self, kingName: str):
//         self.tree = defaultdict(list)
//         self.dead = set()
//         self.king = kingName

//     def birth(self, parentName: str, childName: str) -> None:
//         self.tree[parentName].append(childName)

//     def death(self, name: str) -> None:
//         self.dead.add(name)

//     def getInheritanceOrder(self) -> List[str]:
//         line = []
//         def dfs(name):
//             if name not in self.dead:
//                 line.append(name)
//             for n in self.tree[name]:
//                 dfs(n)
//         dfs(self.king)
//         return line
        


// # Your ThroneInheritance object will be instantiated and called as such:
// # obj = ThroneInheritance(kingName)
// # obj.birth(parentName,childName)
// # obj.death(name)
// # param_3 = obj.getInheritanceOrder()