class Solution {
    public int maxArea(int[] heights) {
        int l= 0;
        int r= heights.length-1;
        int max = (r-l)* Math.min(heights[l],heights[r]);
        int k;
        while(l<r){
            k = (r-l)* Math.min(heights[l],heights[r]);
            max = Math.max(max, k);
            if(heights[l]<heights[r]){
                l++;
            }
            else if(heights[l]>heights[r]){
                r--;
            }
            else{
                l++;
            }

        }

       return max; 
    }
}