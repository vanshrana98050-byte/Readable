class Student {

    int id;
    String name;

    Student(int id, String name) {

        this.id = id;
        this.name = name;
    }

    void display() {

        System.out.println(id + " " + name);
    }
}

public class StudentManagement {
    public static void main(String[] args) {

        Student s1 = new Student(101, "Rahul");
        Student s2 = new Student(102, "Aman");

        s1.display();
        s2.display();
    }
}