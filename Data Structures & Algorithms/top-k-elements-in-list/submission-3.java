
class Solution {
    public int[] topKFrequent(int[] nums, int k) {

        Map<Integer, Integer> map = new HashMap<>();

        // Count frequency
        for (int i = 0; i < nums.length; i++) {
            int c = 0;
            for (int j = 0; j < nums.length; j++) {
                if (nums[i] == nums[j]) c++;
            }
            map.put(nums[i], c);
        }

        // Convert entries to list
        List<Map.Entry<Integer, Integer>> list = new ArrayList<>(map.entrySet());

        // Sort by value DESC (high frequency first)
        list.sort((a, b) -> b.getValue() - a.getValue());

        // Pick first k keys
        int[] result = new int[k];
        for (int i = 0; i < k; i++) {
            result[i] = list.get(i).getKey();
        }

        return result;
    }
}
