public class returntype{
    public static void main(String[] args) {
  int num= printsomething(18);
System.out.println(num);
    }
    public static int printsomething(int num){
        int result = num*100;
        return result;
    }
}
