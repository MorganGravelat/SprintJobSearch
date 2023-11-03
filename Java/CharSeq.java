import java.util.Scanner;

public class DriverClass {

	public static void main(String[] args) {
		int numRows , numColumns;
		int index, start, end;
		char charAtIndex;
		int length;
		String subSequence;

		Scanner myScan = new Scanner(System.in);


		System.out.print("Enter how many rows and how many columns to load: ");
		numRows = myScan.nextInt();
		numColumns = myScan.nextInt();

		Code codeObject = new Code(numRows, numColumns);

		codeObject.loadCodeArray(numRows, numColumns);
		codeObject.printCodeArray(numRows, numColumns);
		// __________________________________________
		System.out.print("\n\nTesting charAt: Enter your index [a number greater or equal to 0 and less or equal to ");
		System.out.print((numRows * numColumns - 1) + "]:");
		index = myScan.nextInt();

		charAtIndex = codeObject.charAt(index);

		System.out.println("The character located at index " + index + " is: " + charAtIndex);

		// __________________________________________
		length = numRows * numColumns;

		System.out.println("\n\nTesting length: there are " + length + " characters.");

		// __________________________________________
		System.out.print("\n\nTesting subSequence: Enter start and end indexes: ");

		start = myScan.nextInt();
		end = myScan.nextInt();

		subSequence = codeObject.subSequence(start, end);
		System.out.println("The subsequuence is: " + subSequence);

		// __________________________________________
		System.out.println("\nGoodbye!");
	}
}
