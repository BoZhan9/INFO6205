public class Solution {
    public int getIndex(int[] nums, int x) {
        int startIdx = 0;
        int endIdx = nums.length - 1;
        int midIdx = (nums.length - 1) / 2;
        while (startIdx <= endIdx) {
            if (x == nums[midIdx]) {
                return midIdx;
            } else if (x > nums[midIdx]) {
                startIdx = midIdx;
            } else {
                endIdx = midIdx;
            }
        }
        return -1;

    }

    public static void main(String[] args) {
        Solution s = new Solution();
        int[] nums = {2,4,4,4,6,7,7,7,8,9,9,9};
        System.out.println(s.getIndex(nums, 7));
    }

}

// Time: O(logn)
// Space: O(1) no extra space
