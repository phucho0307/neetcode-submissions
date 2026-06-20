class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;   // 1️⃣ lengths must match

        int[] count = new int[26];  // 2️⃣ array for each letter (a–z)

        for (int i = 0; i < s.length(); i++) {        // 3️⃣ go through both strings
            count[s.charAt(i) - 'a']++;  // add 1 for letter in s
            count[t.charAt(i) - 'a']--;  // subtract 1 for letter in t
        }

        for (int n : count) {                        // 4️⃣ check all counts
            if (n != 0) return false;   // if any count isn’t zero, not an anagram
        }

        return true;  // 5️⃣ all counts zero → perfect anagram
    }
}
