public class Inversions {
    public static int findInversions(int[] a){
        int count = 0;
        for(int i=0; i<a.length; i++){
            for(int j=i+1;  j<a.length; j++){
                if(a[i] > a[j]) count++;
            }
        }
        return count;
    }
 
    public static void main(String[] args) {
        int a[] = new int[]{90, 20, 30, 40, 50};
        int inversions = findInversions(a);
        System.out.print("Inversions : " + inversions);
    }
}