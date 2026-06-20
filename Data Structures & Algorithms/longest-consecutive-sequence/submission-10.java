class Solution {
    public int longestConsecutive(int[] nums) {
        if (nums.length == 0) return 0;

        List<Integer> list = new ArrayList<>();
        for (int x : nums) list.add(x);

        Collections.sort(list);

        int c = 1;
        int max = 1;

        for (int i = 0; i < list.size() - 1; i++) {
            if (list.get(i).equals(list.get(i + 1))) {
                continue; // skip duplicates
            }
            if (list.get(i) + 1 == list.get(i + 1)) {
                c++;
            } else {
                max = Math.max(max, c);
                c = 1;
            }
        }

        max = Math.max(max, c); // last sequence
        return max;
    }
}
