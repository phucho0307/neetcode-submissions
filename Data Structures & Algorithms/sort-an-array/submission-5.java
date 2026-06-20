class Solution {
    public int[] sortArray(int[] nums) {
        if(nums.length==1) return new int[] {nums[0]};
        int[]l1 = new int[nums.length/2];
        int[]l2 = new int[nums.length - nums.length/2];
        
        for(int i=0; i<nums.length/2;i++){
            l1[i] = nums[i];
        }
        for(int i=0; i<nums.length - nums.length/2;i++){
            l2[i] = nums[nums.length/2+i];
        }
        l1 = sortArray(l1);
        l2 = sortArray(l2);

        int[] ans = merge(l1,l2);
        return ans;
        
    }
    public int[] merge(int[] l1, int[] l2){
        int[]a= l1;
        int[]b= l2;
        int[]ans = new int[a.length + b.length];
        int n=0;
        int k=0;
        int t=0;
        while(n<a.length && k< b.length){
            if(a[n]<=b[k]){
                ans[t]=a[n];
                t++;
                n++;
            }
            else{
                ans[t]=b[k];
                t++;
                k++;       
            }
        }
        while(n<a.length){
            ans[t] = a[n];
            t++;
            n++;
        }
        while(k<b.length){
            ans[t] = b[k];
            t++;
            k++;
        }
        return ans;
    }
}