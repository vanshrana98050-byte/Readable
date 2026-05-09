public class largest{
    public static void main(String[]args){
        int a = 89;
        int b = 23;
        int c = 74;

        if(a>=b && a>=c){
            System.out.println(" A is the largest number");
        }
        else if (b>=c && b>=a){
            System.out.println(" B is the largest number");
        }
        else{
            System.out.println(" C is the largest number");
        }
    }
}