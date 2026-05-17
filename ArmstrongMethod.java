public class ArmstrongMethod {

    static boolean check(int num) {

        int original = num;
        int sum = 0;

        while(num > 0) {

            int digit = num % 10;

            sum += digit * digit * digit;

            num /= 10;
        }

        return sum == original;
    }

    public static void main(String[] args) {

        if(check(153)) {
            System.out.println("Armstrong");
        } else {
            System.out.println("Not Armstrong");
        }
    }
}