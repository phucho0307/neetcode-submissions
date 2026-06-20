class Solution {
    public boolean isPalindrome(String s) {
         for (int i = s.length() - 1; i >= 0; i--) {
            if (!Character.isLetterOrDigit(s.charAt(i))) {
                s = s.substring(0, i) + s.substring(i + 1);
            }
        }
        s= s.toLowerCase();
        for(int i=0; i<s.length()/2;i++){
            if(s.charAt(i) != s.charAt(s.length()-1-i)) return false;
        }
        return true;
        
    }
}

