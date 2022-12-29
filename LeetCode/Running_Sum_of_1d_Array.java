class Running_Sum_of_1d_Array {
    public int[] runningSum(int[] nums) {

        int[] runningSumResult = new int[nums.length];

        runningSumResult[0] = nums[0];

        for (int i = 1; i < nums.length; i++) {

            runningSumResult[i] = runningSumResult[i - 1] + nums[i];

        }

        return runningSumResult;
    }
}