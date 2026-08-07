class Solution {
public:
    int singleNumber(vector<int>& nums) {

        for(int i=0; i<nums.size(); i++) {

            int count = 0;
            int flag = 0;

            for(int k=0; k<i; k++) {
                if(nums[i] == nums[k]) {
                    flag = 1;
                    break;
                }
            }

            if(flag == 1) {
                continue;
            }

            for(int j=0; j<nums.size(); j++) {
                if(nums[i] == nums[j]) {
                    count++;
                }
            }

            if(count == 1) {
                return nums[i];
            }
        }

        return 0;
    }
};