class Solution {
    public boolean hasDuplicate(int[] nums) {
        int a=0;
        for(int i =0; i<nums.length-1;  i++){
            for(int j=i+1; j<nums.length;j++){
                if(nums[i]==nums[j]) a++;
            }
        }
        return a>0;
        
    
}

}