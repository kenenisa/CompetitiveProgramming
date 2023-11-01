class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> lookup;
        for(int i : nums){
            lookup.insert(i);
        }
        int result = 0;
        for(int i : nums){
            if(!lookup.count(i-1)){
                int j = i;
                while(lookup.count(j)){
                    j++;
                }
                result = max(result,j-i);
            }
        }
        return result;
    }
};
