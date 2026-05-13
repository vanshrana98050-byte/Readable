import java.util.Scanner;
public class vovelConsonent{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Please Enter The Word ");
        char ch=sc.next().charAt(0);


        if (ch=='a'|| ch=='e'|| ch== 'i'||ch=='o'||ch=='u'){
            System.out.println("this is a vovel");
        }
        else{
            System.out.println("this is a consonent");
        }
    }
}
