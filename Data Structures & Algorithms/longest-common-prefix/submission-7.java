class Solution {
    public String longestCommonPrefix(String[] strs) {
    if (strs == null || strs.length == 0) return "";
    return longestCommonPrefix(strs, 0);
}
    public String longestCommonPrefix(String[] strs, int a) {
        if (strs[0].isEmpty()) return "";

        int l = a;
        boolean t = true;
        for(int n=0; n< strs.length; n++){
            if(l>strs[n].length()-1 || strs[0].charAt(l) != strs[n].charAt(l)) {
                t =false;
                break;
            }
        }
        if(t==false) return strs[0].substring(0,l);
        else{
            l++;
            return longestCommonPrefix(strs, l);
        }
    
        

        
    }
}