int maxSubArray(int* nums, int numsSize) {
    
    int sum=nums[0];
    int max=nums[0];
    for(int i =1;i<numsSize;i++){
        sum+=nums[i];
    
    if (sum<nums[i]){
        sum=nums[i];
    }
    if(sum>max){
        max=sum;
    }
}
return max;
}