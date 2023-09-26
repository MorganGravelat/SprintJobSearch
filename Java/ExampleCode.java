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

public class Main { // NO fields in the class once main is created inside as a method and just the 1 method of main

	public void nonStaticMethod () { //If within the same class it can be public or private it won't matter
		System.out.println("I am from the Non Static Method");
	}

	public static void staticMethod() { //TEST TEST TEST you have to know how to access private fields from outside the class with getters and setters
		System.out.println("I am from the Static Method...");
	}

	public void anotherNonStaticMethod() {
		nonStaticMethod(); //Non static methods can call others with no problem
	}

	int nonStaticInt; //initialized as 0
	static int staticInt; // static int ! int static

	public static void main(String[] args) {

		int nonStaticData;
		static int staticData;

		//You can run MyClass statmethods without an object of that class inside this class Main
		//MyClass.staticMethod(); //This will run the static method even before object creation because it is static

		//MyClass myObject = null;
		//((MyClass)null).staticMethod(); //Even type converting a null object into an object MyClass is enough to make the static work USELESS BUT FUN TO KNOW
		MyClass myObject = new MyClass();
		//myObject.staticMethod();
		myObject.nonStaticMethod(); // You need the created myObject to run this one


	}
}


class MyClass {
	public static void staticMethod() { //If you want all objects of that class to say the same thing make it static
		System.out.println("From the Static Method...");
	}

	public void nonStaticMethod() {
		System.out.println("From the NON-Static Method...");
	}
}

//Working with OOP concepts
//NEXT PROJECT
import java.util.ArrayList;

class DriverClass {
    public static void main(String[] args) {

        String fullName = "Erika T. Jones";
        String employeeNumber = "ej789";
        double payRate = 10.50, hoursWorked = 36;

        Employee e;
        e = new Employee(fullName, employeeNumber, payRate, hoursWorked);

        System.out.println(e); //Testing toString

        e.printCheck(); //This prints the check of Erika T. Jones

        Company company = new Company();

        company.hire(new Employee("Saeed Happy", "sh895", 200, 2));
        company.hire(e);

        company.printCompanyInfo();

        company.hire(new Employee("Enrico Torres", "et897", 150, 4));
        company.hire(new Employee("Walid Williams", "ww547", 150, 3));

        System.out.println("Number of employees excluding the boss: " + company.countEmployees(600));

        //Add as many employees as you want
        //give each employee a unique employee number

        company.printCheck("ej789");

        company.deleteEmployeesBySalary(600);

        company.reverseEmployees();

        System.out.println(company.SearchByName("WaLiD WiLLiAms"));

        company.printEmployees();

        System.out.println("Bye!");

    }

}
class Employee {
    private String fullName;
    private String employeeNumber;
    private double payRate;
	private double hoursWorked;

    public String getFullName() {
		return fullName;
	}

	public void setFullName(String fullName) {
		this.fullName = fullName;
	}

	public String getEmployeeNumber() {
		return employeeNumber;
	}

	public void setEmployeeNumber(String employeeNumber) {
		this.employeeNumber = employeeNumber;
	}

	public double getPayRate() {
		return payRate;
	}

	public void setPayRate(double payRate) {
		this.payRate = payRate;
	}

	public double getHoursWorked() {
		return hoursWorked;
	}

	public void setHoursWorked(double hoursWorked) {
		this.hoursWorked = hoursWorked;
	}


    public Employee( String fullName, String employeeNumber, double payRate, double hoursWorked ) {
    	this.fullName = fullName;
    	this.employeeNumber = employeeNumber;
    	this.payRate = payRate;
    	this.hoursWorked = hoursWorked;
    }

	public double grossPay () {
		return payRate * hoursWorked;
	}

    private double netPay () {
    	return (this.grossPay()) * .94;
    }

    public void printCheck () {
    	System.out.printf("%.2f",netPay());
    }

    @Override
    public String toString () {
    	return String.format("[%s/%s, %.0f Hours @ %.1f per hour]",
    			employeeNumber, fullName, hoursWorked, payRate);
    }
}

//Starting work on company class
class Company {
    private ArrayList<Employee> employeeList;

    private String companyName;
    private static String companyTaxId;

    public static String getCompanyTaxId() {
		return companyTaxId;
	}

	public static void setCompanyTaxId(String companyTaxId) {
		Company.companyTaxId = companyTaxId;
	}

	public String getCompanyName() {
		return companyName;
	}

	public void setCompanyName(String companyName) {
		this.companyName = companyName;
	}

	public Company() {
        employeeList = new ArrayList<>();
        companyName = "People's Place";
        companyTaxId = "v1rtua7C0mpan1";
    }

    public boolean hire (Employee employee) {
    	//This method adds an employee to the array list unless they have an employee number that is already used
    	for (Employee e : employeeList) {
    		if (e.getEmployeeNumber() == employee.getEmployeeNumber()) return false;
    	}
    	employeeList.add(employee);
    	return true;
    }

    public void printCompanyInfo() {
    // This method prints the company name, the tax id and the current number of employees
    // You may choose to print that any way you like!
    	System.out.printf("\n[Company Name: %s | Company Tax Id: %s | Number of Employees: %d]\n",
    			companyName, companyTaxId, employeeList.size());
    }

    public void printEmployees() {
        //This methods prints all employees (One employee per line)
        //Note that you already have toString in Employee
    	for (Employee e : employeeList) {
    		System.out.println(e);
    	}
    }

    public int countEmployees( double maxSalary ) {
        //This method returns the number of employees paid less than maxSalary
    	int count = 0;
    	for (Employee e : employeeList) {
    		if ((e.grossPay()) != maxSalary) count++;
    	}
    	return count;
    }
 public boolean SearchByName (String fullName) {
        //This method returns true if fullName exists as an employee
        //It returns false otherwise
        //this is a not a case sensitive search.
    	for (Employee e : employeeList) {
    		if (e.getFullName().equalsIgnoreCase(fullName)) return true;
    	}
    	return false;
    }

    public void reverseEmployees () {
        //This method reverses the order in which the employees were added to the list
        //The last employee is swapped `with the first employee, the
    	//second last with the second and so on..`
    	int first = 0;
    	int last = employeeList.size() - 1;

    	for (;first < last;first++,last--) {
    		Employee emp = employeeList.get(first);
    		employeeList.set(first, employeeList.get(last));
    		employeeList.set(last, emp);
    	}
    }

    public void deleteEmployeesBySalary (double targetSalary){
        //This method deletes all employees who are paid targetSalary as a gross salary
    	for (Employee e : employeeList) {
    		if (e.grossPay() == targetSalary) employeeList.remove(e);
    	}
    }

    public void printCheck ( String employeeNumber) {
        Employee emp = null;
        String fString = "";
        for (Employee e : employeeList) {
        	if (e.getEmployeeNumber().equalsIgnoreCase(employeeNumber)) {
        		emp = e;
        	}
        }
        if (emp == null) {
        	System.out.println("NO SUCH EMPLOYEE EXISTS");
        }
        else {
        	fString = String.format("%s\n%28s:%25s\n%30s:%14s\n%31s:%13.2f\n"
        			+ "%25s:%19.2f\n\n%28s:		$%.2f\n\n%23s\n%22s: $%20.2f\n\n%20s: %24.2f Dollars\n\n%s",
        			"	-----------------------------------------------------------",
        			"Employee's name", emp.getFullName(), "Employee's number", emp.getEmployeeNumber(), "Hourly rate of pay", emp.getPayRate(),
        			"Hours worked", emp.getHoursWorked(), "Total Gross Pay", emp.grossPay(),"Deductions",
        			"Tax (6 %)", (emp.grossPay()*.06),"Net Pay", (emp.grossPay() * .94),
        			"	-----------------------------------------------------------");
        	System.out.println(fString);
        }

    }
} //End of class Company
////////////////NEXT FILE
//PRACTICE TEST
public class Question {
	/* 8 Test Attempt 1
	public static void main(String args[]) {
        String[] name = new String[3]; // Array of size 3 [0 / 1 / 2]
        int i = 0;

        for (i = 0; i < 3; i++) // i = 0/1/2/ENDS UP 3
            name[i] = new String("Abc");

        System.out.println(i + " Outside");
        name[i] = new String("Xyz"); //THIS BREAK HAHAHA name[3] is outside the bounds of the name array
        System.out.println(name[i-1]);
        for (i = 0; i < 4; i++) {
        	if (i < 3)
        		System.out.println(i + name[i]);
        }
    }
    */
	/* 1

		public static void main(String args[]) {
			int five = 5;
			String name = "hi";
			System.out.println( 5 + 6 * 2 + name + five + 4 + 5 ); //Before you can add any number together but after the string comes in it all gets added into a string.
		}
	*/
	/* 2
	public static void main(String args[]) {
		Employee[] company;
		company = new Employee [3];
		for (Employee e: company) //Employee e is a temporary variable that represents the data of the Employees in the array so it will be null in the end
			e = new Employee ();
		for (int i = 0; i<3; i++)
			System.out.print(company [i]);
		}
	*/
	/* 3
	public static void main(String args[]) {
		SimpleClass simpleRef1, simpleRef2, simpleRef3;

		simpleRef1 = new SimpleClass(1);
		simpleRef2 = new SimpleClass(2);
		simpleRef3 = new SimpleClass(3);

		System.out.println(simpleRef1.hashCode());
		System.out.println(simpleRef2.hashCode());
		System.out.println(simpleRef3.hashCode() + "\n");
		simpleRef1 = simpleRef2; //Memory address of
		simpleRef2 = simpleRef3;
		simpleRef3 = simpleRef1;
		System.out.println(simpleRef1.hashCode()); //simpleRef1 & 3 are pointing to the old simpleRef2
		System.out.println(simpleRef2.hashCode()); //Thus 1 and 3 are going to have the same hashCode as old two
		System.out.println(simpleRef3.hashCode()); //2 was set to 3 before this happened so 2 is the old 3 now

		System.out.print(simpleRef3);
		System.out.print(simpleRef2);
		System.out.println(simpleRef1); //This will print out the numbers 232 since 1 and 3 now contain simpleData = 2 and 2 is simpleData = 3
	}
	*/
	/* 4
	private int val;
	private void method1 () {
		method2();
		val = 1;
	}
	public static void main(String args[]) {
		Question q = new Question ();

		q.method1();
		method2();
	}
	private static void method2() {
		System.out.print((new Question()).val + " "+ new Question()); //5 65 6 will print in the end
	}

	public Question () {
		val = 5; //on each new creation val=5 so when it is set to 1 then a new one is created the val goes back to 5 before printing
	}

	public String toString() {
		return "6";
	}
	*/
	/*5
	public static void main(String args[]) {
		Test t1 = new Test(); //Test() is not a method of Test and so this will error here
		Test t2 = t1;
		t2 = new Test(2,1);
		t1 = t2;
		System.out.println(t1.x + " " + t2.y);
	}

	*/

	/*6
	public static void main(String args[]) {
		String s1 = "abc";
		String s2 = "abc";
		//System.out.println(s1.hashCode() + " " + s2.hashCode());
		String s3 = new String("abc"); //Same hash code but a different memory address than the two string literals.
		//System.out.println(1==1);

		System.out.print("A");
		if (s1 == s2) { //s1 and s2 are string literals and thus will == eachother
			if (s1 != s3) { //s1 and s3 are different types s1 a string literal and s3 is created as a new making it an object with a seperate memoryu address.
				if (s2 == s3) //string literal vs Object string
					System.out.print("B"); //no else so only A prints
			} else
				System.out.print("C");
		}
	}
	*/
	/*7
	public static void main(String args[]) {
		Test t = new Test();
		System.out.println(Test.x + " " + Test.y); //The fields x and y are not visible outside of the class since they are private.
	}
	*/
	/*8
	public static void main(String args[]) {
		String[] name = new String[3];
		int i = 0;

		for (i = 0; i < 3; i++)
			name[i] = new String("Abc");

		name[i] = new String("Xyz"); //name[3] does not exist

		for (i = 0; i < 4; i++) {
			if (i < 3)
				System.out.print(name[i]);
		}
	}
	*/
    /*9
	private static int val;
	private void method1 () {
		method2();
		val = 1;
	}
	public static void main(String args[]) {
		Question q = new Question ();

		q.method1();
		method2();
	}
	private static void method2() {
		System.out.print((new Question()).val + " " + new Question());
	}

	public Question() {
		val = 5;
	}

	public String toString() {
		return "6";
	}
	*/
	/*10
	public static int doSomething (int a, int b) {
		return ++a + --b; //++ before the var affects it before and ++ after affects it immediately after reading it
		//3 + 0
	}
	public static void main (String args[]) {
		int x = 2, y=1;
		y = doSomething( x , y); // y = 3
		System.out.println(x + "" + y); //2+""+3 remember addition does not work after a string is introduced concat
	}
	*/
	/*11
	public static void main(String args[]) {
		int counter = -1; //pointless the loop sets it to 1
		for (counter = 1; counter <= 3; counter++) { //runs counter = 1/2/3/4 when 4 counter <= 3 procs and the loops is done
			if (counter <= 1) { //If the counter was < 3 instead of <=
				System.out.print("UCF");//Starting at 1 this will print the first run of the loop
				//break;
			}
		}
		if (counter == 4) //counter = 4 after loop so this prints
			System.out.print("UCF");
	}
	*/
	/*12
	public static void main(String args[]) {
		int x = 2, y =3;
		System.out.println( x+y/x+y); //Order of operations are / before + so 2+3/2+3 is actually 2+1+3 OR 6 since there is no 3.0 the number is an int so 3/2 is 1
	}
	*/
	/*13
	public static void main(String args[]) {
		Test t1 = new Test(5, 7);
		Test t2 = new Test(1, 2) , t3 = null;
		System.out.println(t1.hashCode() + " " + t2.hashCode());
		t3 = t2;
		t2 = t1;
		t1 = t3;
		t3 = t1;
		System.out.println(t1.hashCode() + " " + t2.hashCode() + " " + t3.hashCode());
		t2.print(); // Since t2 = t1 print uses 5 + 7
	}
	*/
	/*14
	public static void main(String args[]) {
		String name1 = new String("Jon");
		String name2 = name1;
		//System.out.println(name1.hashCode() + " " + name2.hashCode()); //pointless since hash code just identified the object but not he address
		name1 = new String("Jon"); //This creates a new address in memory for name1 so
		System.out.println(name1 == name2); //These two have different memory addresses if they were "Jon" the string literal it would be true
	}
	*/

	/*15
	public static void main(String args[]) {
		for (int counter = 1; counter < 6; counter++) {
			System.out.print(counter);
			if (counter > 2 || counter > 3) {
				continue;
			}
			System.out.print("UCF"); //Works for counter 1/2 then continues through each for loop
		}
		System.out.print("UCF"); //Going to run once
	}
	*/
	/*16
	public static void main(String args[]) {
		Employee [] company;
		company = new Employee[3];

		for (Employee e : company) {
			//e = new Employee(); This would allow the word employee to print over and over
			System.out.print(e); //Without the new employee being set to each e it will just be null
		}
	}
	*/
	/*17
	public static void main(String args[]) {
		MyClass myObject = new MyClass(true);
		System.out.println(myObject); //Since the toString is overrided to print "false" it will print "false"
	}
	*/

}



/*2
class Employee {
	public String toString() {
		return "employee";
	}
}
*/
/*3
class SimpleClass {
	public int simpleData;

	public SimpleClass (int simpleData) {
		this.simpleData = simpleData;
	}

	@Override
	public String toString() {
		return simpleData + "";
	}
}
*/
/*5

class Test {
	public int x,y;
	public Test(int x, int y) {
		this.x = 1;
		this.y = 2;
	}
	public Test(int x) {
		this.x = x;
		this.y = x;
	}
}
*/
/*7
class Test {
	private static int x, y;

	public Test() {
		x = 1;
		y = 2;
	}
}
*/
/*13
class Test {
	private int x, y;

	public void setAll(int x , int y) {
		this.x = x;
		this.y = y;
	}

	public Test(int x, int y) {
		this.y = y;
		this.x = x;
	}

	public void print() {
		System.out.println(x + y);
	}
}
*/
/*16
class Employee {
	public String toString() {
		return "employee";
	}
}
*/
/*17
class MyClass {
	private boolean goAgain;

	public MyClass(boolean goAgain) {
		this.goAgain = goAgain;
	}

	@Override
	public String toString() {
		return "false";
	}
}
*/
