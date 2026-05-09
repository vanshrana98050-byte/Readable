public class smallest{
    public static void main(String[]args){
        int a = 89;
        int b = 23;
        int c = 74;

        if(a<=b && b<=a){
            System.out.println(" A is the smallest number");
        }
        else if (b<=c && b<=a){
            System.out.println(" B is the smallest number");
        }
        else{
            System.out.println(" C is the smallest number");
        }
    }
}