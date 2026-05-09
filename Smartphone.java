public class Smartphone{

    String brandname="apple";
    String colour= "graphie";
    String modelname= "iphone12 pro max";
    int price=100000;
    int screensize=6;


    public void details(){
      System.out.println("this is the brandname "+brandname);
      System.out.println("this is the colour "+colour);
      System.out.println("this is the modelname "+modelname);
      System.out.println("this is the price "+price);
      System.out.println("this is the screensize "+screensize);
    }


    public void turnOn(){
        System.out.println("the smartphone is tyrning on ");
    }


    public void turnOff(){
        System.out.println("the smartphone is turning off");
    }


    public void call(){
        System.out.println("the smartphone is ringing");
    }


    public static void main(String[] args){
        Smartphone phone1; 
        phone1= new Smartphone();
        phone1.brandname="apple";
        phone1.modelname="iphone 12 pro max";
        phone1.screensize=6;
        phone1.price=100000;
        phone1.colour="graphite";


        phone1.turnOff();
        phone1.turnOn();
        phone1.call();
        phone1.details();
        }    
    }

