class Solution {
public:
    void sortColors(vector<int>& nums) {

        int count[3]{};
        for(int n : nums){
            count[n]++;
        }
        int i = 0;
        for(int k = 0; k < 3;k++){
            for(int j = 0; j < count[k];j++){
                nums[i+j] = k;
            }
            i += count[k];
        }
    }
};
