import java.io.IOException;

public class ThrowsDemo {

    static void check() throws IOException {

        throw new IOException("Input Output Exception");
    }

    public static void main(String[] args) {

        try {

            check();
        }

        catch(Exception e) {

            System.out.println(e);
        }
    }
}