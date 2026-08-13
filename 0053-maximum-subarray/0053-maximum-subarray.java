class Solution {
    public int maxSubArray(int[] nums) {
        int csum = 0;
        int msum = Integer.MIN_VALUE;
        for(int r = 0; r < nums.length; r++) {
            if(csum < 0) csum = 0;
            csum += nums[r];
            if(msum < csum) msum = csum;
        }
        return msum;
    }
}