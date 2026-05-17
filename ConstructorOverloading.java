class Rectangle {

    int length;
    int width;

    Rectangle() {

        length = 0;
        width = 0;
    }

    Rectangle(int l, int w) {

        length = l;
        width = w;
    }

    void area() {

        System.out.println("Area = " + (length * width));
    }
}

public class ConstructorOverloading {
    public static void main(String[] args) {

        Rectangle r1 = new Rectangle();

        Rectangle r2 = new Rectangle(10, 5);

        r1.area();
        r2.area();
    }
}