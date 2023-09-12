
class OneA {
    public static int m1() {
        return 100;
    }
}

public class One {
    public int invoke() {
        int rtv = OneA.m1();
        return rtv;
    }
}
