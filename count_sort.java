public class demo
 {
    public static int[] countsort(int[] inputarray) {
        int N = inputarray.length;
        int M=0;

        for (int i=0;i<inputarray.length;i++){
            M=Math.max(M,inputarray[i]);
        }
        int [] count = new int[M+1];
        for (int i=0;i<inputarray.length;i++){
            count[inputarray[i]]+=1;
        }
        for (int i = 1; i <= M; i++) {
            count[i] += count[i - 1];
        }
        int[] outputarray = new int[N];
        for(int i=N-1;i>=0;i--){
            outputarray[count[inputarray[i]]-1] =inputarray[i];
            count[inputarray[i]]--;

        }
        return outputarray;
    }   
    public static void main(String arg[])
    {
        int[] inputarray = {4, 3, 12, 1, 5, 5, 3, 9};
        int [] outputarray = countsort(inputarray);
        for (int i=0;i<inputarray.length;i++){
            System.out.print(outputarray[i]+" ");
        }
    }
    
}
