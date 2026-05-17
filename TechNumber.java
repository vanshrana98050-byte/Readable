public class TechNumber {
    public static void main(String[] args) {

        int num = 2025;

        String str = String.valueOf(num);

        int len = str.length();

        if(len % 2 == 0) {

            int first = Integer.parseInt(str.substring(0, len / 2));
            int second = Integer.parseInt(str.substring(len / 2));

            int sum = first + second;

            if(sum * sum == num) {
                System.out.println("Tech Number");
            } else {
                System.out.println("Not Tech Number");
            }
        }

        else {
            System.out.println("Not Tech Number");
        }
    }
}