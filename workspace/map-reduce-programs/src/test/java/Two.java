
class TwoA {

    TwoA(String s){
        System.out.println("---");
    }
    public int getValue(){
        return 100;
    }
}
public class Two {
    TwoA obj;

    Two(){
        obj = new TwoA("");
    }

    public int getValue(){
        return obj.getValue();
    }
}
