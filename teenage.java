import java.util.Scanner;
public class teenage{
    public static void main(String[]args){
Scanner sc = new Scanner(System.in);
System.out.println("Please Enter Your Age");

int age=sc.nextInt();
if (age>19){
    System.out.println("You Are Not A Teenager");
}

else{
    System.out.println("You Are A Teenager");
}
sc.close();

    }
}