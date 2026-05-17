public class MultipleCatch {
    public static void main(String[] args) {

        try {

            int a = 10 / 0;

            System.out.println(a);
        }

        catch(ArithmeticException e) {

            System.out.println("Arithmetic Error");
        }

        catch(Exception e) {

            System.out.println("General Error");
        }
    }
}