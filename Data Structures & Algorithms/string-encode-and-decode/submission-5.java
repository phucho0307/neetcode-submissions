class Solution {
    List<Integer> k = new ArrayList<>();

    public String encode(List<String> strs) {
        String str = "";
        for(String i : strs){
            str+= i;
            k.add(i.length());
        }
        return str;
    }

    public List<String> decode(String str) {
        List<String> h = new ArrayList<>();

        for(int i: k){
             h.add(str.substring(0,i));
             str = str.substring(i);
        }
        return h;

    }
}
