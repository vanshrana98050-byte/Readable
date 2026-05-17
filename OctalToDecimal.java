public class OctalToDecimal {
    public static void main(String[] args) {

        int octal = 31;

        int decimal = 0;

        int power = 0;

        while(octal > 0) {

            int digit = octal % 10;

            decimal += digit * Math.pow(8, power);

            octal /= 10;

            power++;
        }

        System.out.println("Decimal = " + decimal);
    }
}