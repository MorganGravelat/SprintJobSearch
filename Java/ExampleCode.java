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
