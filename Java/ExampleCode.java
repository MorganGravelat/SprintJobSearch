import java.util.Scanner;

public class Main {
	public static void main (String [] array) {
		int x = 4;
		int y = x-- + 1;

		System.out.println(y);
		/*String numbers;
		String [] items;
		int num1 , num2;
		Scanner myScan = new Scanner ( System.in);

		System.out.print("Enter your two integers in the format x-y:");
		numbers = myScan.nextLine();

		items = numbers.split("-");

		num1 = Integer.parseInt(items[0]);
		num2 = Integer.parseInt(items[1]);

		System.out.println("You have " + num1 + " " + num2);

		System.out.println(num1 + "+" + num2 + " = " + (num1+num2)); //not encasing the nums in () will cause it to append 55 instead of 10
		System.out.println(num1 + "*" + num2 + " = " + (num1*num2));
		System.out.println(num1 + "/" + num2 + " = " + ((double)num1/num2) );//(double) is a temporary type cast
		System.out.println(num1 + "/" + num2 + " = " + (num1%num2) );
		*/
		//System.out.printf("[%10.2f]", 120.231254); //just like in c conversion specifiers

		//	String name1 = "abc", name2 = "abc";
		//	if ( name1 == name2 ) System.out.println("Same");
		//	else System.out.println("Not the Same");
		//	String name1 = "abc", name2 = new String("abc");
		//	if ( name1.compareTo(name2) == 0 ) System.out.println("Same");
		//	else System.out.println("Not the Same");
		//	String name1 = "abc", name2 = new String("aBc");
		//	if ( name1.compareToIgnoreCase(name2) == 0 ) System.out.println("Same");
		//	else System.out.println("Not the Same");
			//String name1 = "abc", name2 = new String("abc");
			//if ( name1.equals(name2) == true ) System.out.println("Same");
			//else System.out.println("Not the Same");
	}
}
