class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashSet<Integer> set = new HashSet<>();
        for(int ele : nums)
            set.add(ele);

        return nums.length != set.size();
        


    }
}