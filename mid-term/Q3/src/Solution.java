public class Solution {
    public static void main(String[] args) {
        Solution s = new Solution();
        int[] nums = {0,1,0,1,1,0,1,1,1,0,0,0};
        System.out.println(s.getMaxConsecutiveOnes(nums));
    }
    public int getMaxConsecutiveOnes(int[] nums) {
        int longest = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != 1) {
                continue;
            }
            int count = 0;
            for (int j = i; j < nums.length; j++) {
                if (nums[j] == 1) {
                    count++;
                } else {
                    break;
                }
            }
            if (longest < count) {
                longest = count;
            }


        }
        return longest;

    }
}

// Time: O(n)
// Space: O(1) no extra space
