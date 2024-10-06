import java.util.Scanner;
public class grades
{
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int m=sc.nextInt();
        int s=sc.nextInt();
        if(n>50 && m>60 && s>100)
        {
            System.out.println("10");
        }
        else if(n>50 && m>60)
        {
            System.out.println("9");
        }
        else if(m>60 && s>100)
        {
            System.out.println("8");
        }
        else if(n>50 && s>100)
        {
            System.out.println("7");
        }
        else if(n>50 || m>60 || s>100)
        {
            System.out.println("6");
        }
        else{
            System.out.println("5");
        }
    }
}