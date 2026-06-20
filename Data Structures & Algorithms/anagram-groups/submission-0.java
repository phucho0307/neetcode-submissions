
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> map = new HashMap<>();

        for (String s : strs) {
            // Convert string to char array, sort it, convert back
            char[] chars = s.toCharArray();
            Arrays.sort(chars);
            String key = new String(chars);

            // Insert into map
            map.putIfAbsent(key, new ArrayList<>());
            map.get(key).add(s);
        }

        return new ArrayList<>(map.values());
    }
}
