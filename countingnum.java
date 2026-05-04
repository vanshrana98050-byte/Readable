public class countingnum{
    public static void main(String[] args) {
        String str="abcdefghijklmnopqrstuvwxyz";
        int n=str.length();
        for (int i=0;i<n;i++){
            char ch = str.charAt(i);
            System.out.println("this number    "+i+"     of     "+ch);
        }
    }
}
