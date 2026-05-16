import java.util.HashMap;

public class HashMapDemo {
    public static void main(String[] args) {

        HashMap<Integer, String> map = new HashMap<>();

        map.put(101, "Rahul");
        map.put(102, "Aman");
        map.put(103, "Priya");

        System.out.println(map);
    }
}