import java.util.Scanner;

public class REmove {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter String: ");
        String str = sc.nextLine();

        str = str.replaceAll("\\s", "");

        System.out.println("Output = " + str);
    }
}