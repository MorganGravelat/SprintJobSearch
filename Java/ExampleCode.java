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
////////////////NEXT FILE
import java.util.Scanner;

public class main {

	public static void main(String[] args) {
		String student_id = ""; //Setting up variables for the program requirements
		String full_name = "";
		String first_class = "";
		String second_class = "";
		String [] class_one_arr;
		String [] class_two_arr;
		String crn1, crn2;
		int credits1, credits2;
		double cost1, cost2;
		Scanner stringScanner = new Scanner(System.in);

        System.out.print("Enter the Student's Id: ");
		student_id = stringScanner.nextLine();
		System.out.print("Enter the Student's full name: ");
		full_name = stringScanner.nextLine();

		System.out.print("\nEnter crn/credit hours for the first class(like 5665/3): ");
		first_class = stringScanner.nextLine();
		class_one_arr = first_class.split("/");
		crn1 = class_one_arr[0];
		credits1 = Integer.parseInt(class_one_arr[1]);

		System.out.print("Enter crn/credit hours for the second class(like 5665/3): ");
		second_class = stringScanner.nextLine();
		class_two_arr = second_class.split("/");
		crn2 = class_two_arr[0];
		credits2 = Integer.parseInt(class_two_arr[1]);
		//System.out.println(student_id + " " + full_name + " FirstClass" + first_class + " SecondClass" + second_class);

		cost1 = credits1 * 120.25;
		cost2 = credits2 * 120.25;

		System.out.print("\nThank you!\nFee invoice prepared for: " + full_name);
		//System.out.print(full_name);

		System.out.print("\n\n		SIMPLE COLLEGE\n		ORLANDO FL 10101\n		"
				+ "*************************		\n\n		Fee Invoice Prepared for:\n"
				+ "		[" + full_name + "]" + " [" + student_id + "]\n\n"
				+ "		1 Credit Hour = $120.25");

		System.out.printf("\n\n		%-8s %-6s", "CRN", "CREDIT HOURS");
		System.out.printf("\n		%-8s %-6d 		$%-10.2f", crn1, credits1, cost1);
		System.out.printf("\n		%-8s %-6d 		$%-10.2f", crn2, credits2, cost2);
		System.out.printf("\n\n			 %10s", "Health & id fees	$35.00");
		System.out.printf("\n\n		----------------------------------------");
		System.out.printf("\n			Total Payments" + "		$%.2f", (cost1 + cost2 + 35));

	}

}
////////////////NEXT FILE
