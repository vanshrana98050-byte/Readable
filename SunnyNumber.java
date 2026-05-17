public class SunnyNumber {
    public static void main(String[] args) {

        int num = 8;

        int next = num + 1;

        int sqrt = (int)Math.sqrt(next);

        if(sqrt * sqrt == next) {
            System.out.println("Sunny Number");
        } else {
            System.out.println("Not Sunny Number");
        }
    }
}