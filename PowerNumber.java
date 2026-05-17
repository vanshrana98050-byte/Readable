public class PowerNumber {
    public static void main(String[] args) {

        int base = 2;
        int power = 5;

        int result = 1;

        for(int i = 1; i <= power; i++) {

            result *= base;
        }

        System.out.println("Result = " + result);
    }
}