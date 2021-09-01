public class temp {
    // public int factorial(int inpt) {
    // int res = 1;

    // while (inpt != 1) {
    // res *= inpt;
    // inpt -= 1;
    // }

    // return res;
    // }

    public int factorial(int inpt) {
        if (inpt == 1){
            return 1;
        }

        return inpt*factorial(inpt-1);
    }

    public static void main(String[] args) {
        temp tmp = new temp();
        int inpt = 5;

        System.out.println(tmp.factorial(inpt));
    }
}