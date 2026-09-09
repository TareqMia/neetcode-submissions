class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> hashSet = 
        Arrays.stream(nums)
        .boxed()
        .collect(Collectors.toSet());
        return hashSet.size() < nums.length;  

    }
}