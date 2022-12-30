import java.util.Arrays;

class Running_Sum_of_1d_Array {
    public int[] runningSum(int[] nums) {
        int[] runningSumResult = new int[nums.length];

        runningSumResult[0] = nums[0];

        for (int i = 1; i < nums.length; i++) {

            runningSumResult[i] = runningSumResult[i - 1] + nums[i];

        }

        return runningSumResult;
    }

    public static void main(String[] args) {
        Running_Sum_of_1d_Array myobj = new Running_Sum_of_1d_Array();
        // int[] inpt = new int[4];
        // inpt[0] = 1;
        // inpt[1] = 2;
        // inpt[2] = 3;
        // inpt[3] = 4;

        int[] inpt = { 1, 2, 3, 4 };

        int[] opt = { 1, 3, 6, 10 };

        int[] result = myobj.runningSum(inpt);

        System.out.println("result = " + Arrays.toString(result));

        System.out.println(Arrays.equals(result, opt));
    }
}