import java.util.Arrays;

class Find_pivot_index {
    public int pivotIndex(int[] nums) {
        int result = -1;
        int totalSum = Arrays.stream(nums).sum();
        int lSum = 0;

        for (int idx = 0; idx < nums.length; idx++) {
            int currNo = nums[idx];
            int rSum = totalSum - lSum - currNo;

            if (lSum == rSum)
                return idx;

            lSum += currNo;
        }

        return result;
    }

    public static void main(String[] args) {
        Find_pivot_index myobj = new Find_pivot_index();
        int[] inpt = { 1, 7, 3, 6, 5, 6 };
        int opt = 3;
        int result = myobj.pivotIndex(inpt);

        System.out.println("result = " + result);

        System.out.println(result == opt);
    }
}