import java.util.*;
class StringReverse
{
    void reverse(String s)
    {
        if ((s==null)||(s.length() <= 1))

            System.out.println(s);

        else

        {

            System.out.print(s.charAt(s.length()-1));
            reverse(s.substring(0,s.length()-1));

        }

    }

    public static void main(String[] args)

    {
        Scanner sc = new Scanner(System.in);

        String s = sc.nextLine();

        StringReverse rev = new StringReverse();

        rev.reverse(s);

    }
}
