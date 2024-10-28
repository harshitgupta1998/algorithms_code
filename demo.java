public class demo
 {
    public static void main(String arg[])
    {
        int n=3;
        int val=fact(n);
        System.out.println(val);
    }
    public static int fact(int n){
        
        if (n==0 || n==1){
            return 1;
        }
        int ans=n*fact(n-1);
        return ans;
    }
}
