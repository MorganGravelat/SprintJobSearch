
class Company {

	private Employee [] list;

	public Company() {
		list = new Employee[100];
		for (int index = 0; index < 100; index++) {
			list[index] = null;
		}
	}
	//_________________________________________
	public void hire ( Employee e ) {
		boolean full = true;
		for (int index = 0; index < 100; index++) {
			if ( list[index] == null) {
				list[index] = e;
				full = false;
				break;
			}
		}
		if ( full ) System.out.println("Sorry hiring is not allowed at this time...");

	}
	//__________________________________________

	public void printList () {
		System.out.println(" L I S T  O F  E M P L O Y E E S...");
		for ( Employee e: list )
			if ( e!=null )
				System.out.println(e);
	}

	//______________________________________
	public void fire (String name) {
//		for ( int index = 0; index < 100; index++) {
//			if ( list[index] != null && name.compareToIgnoreCase(list[index].getName()) == 0 ) {
//				//list.remove(index);
//				list[index] = null;
//			}
//		}
		int index = searchByName(name);
		if (index != -1)
		list[index] = null;
	}
}

public class Driver {
	public static void main(String[] args) {

		Company c = new Company();
		c.hire( new SalaryPaid ("Erick Johnson", 14589) );

		c.printList();

		c.fire("Erick Johnson");
		c.printList();
//		Employee e = new HourlyPaid("John Jonhson", 45, 36);
//		e.printCheck();
//		Employee s = new Supervisor("James Jink", 20000, 50000);
//		s.printCheck();
//		System.out.println(s);
		//HourlyPaid hp;
		//Employee hp;
		//Object genericRef = null;
		//hp = new HourlyPaid("Erik Edwqaards", 5, 20);
		//Employee e = null;

		//genericRef = new HourlyPaid("Erik Edwqaards" , 1 , 10);
		//genericRef.printCheck(); //NMOT WORKING
		//genericRef = new String ("Hi");
		//e = new HourlyPaid("Erik Edwqaards" , 1 , 10);

		//genericRef = new String ("Hi");
		//System.out.println(e); //THis will print the HourlyPaid print statement

		//hp.printCheck();
		//hp.setName("Erika J. Jones");
//		Supervisor r = new Supervisor();
//
//		r.abcd();
//		Employee [] array;
//
//		array = new Employee[1000];
//
//		array[69] = new Supervisor("Erik Jones" , 89, 23.5);
//
//		array[69].printCheck();
//
//		array[69] = new HourlyPaid("Jenna Jones", 10, 10);
//
//		array[69].printCheck();
//
//		for ( int i = 0; i < 1000; i++) {
//			array[i] = null;
//		}
		//Employee e;

		//e = new Supervisor("Jimmy Jones", 1200, 25.5);

		//e = new SalaryPaid ("Emma Edwards", 1500);

//		if ( e instanceof Supervisor) {
//			System.out.println("e is referrencing a supervisor object");
//		}
//		else System.out.println("e is referrencing a non supervisor object");
		//System.out.println(e.getClass());

		//e.setName("Jim Jones");

		//((Supervisor)e).setBonus(30.7); //only works if the class is inheriting employee
		//e.printCheck();

	}
}
//_________________

abstract class Employee {

//	public static void abc () {
//		System.out.println("I am from Employee...");
//	}
	private String name;

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}
	public Employee() {
		name = "NO NAME";

	}
	public Employee ( String name) {
		this.name = name;
	}
	public String toString () {
		return "[" + name + "]";
	}
//	public void someMethod() {
//		System.out.println("Some stuff from the Employee Class...");
//	}
	abstract public void printCheck();


}
//____________________________________
class HourlyPaid extends Employee {	//HourlyPaid is an Employee

	private int hoursWorked;
	private double wage;

	public int getHoursWorked() {
		return hoursWorked;
	}

	public void setHoursWorked(int hoursWorked) {
		this.hoursWorked = hoursWorked;
	}

	public double getWage() {
		return wage;
	}

	public void setWage(double wage) {
		this.wage = wage;
	}

	@Override
	public String toString() {
		return "HP -->" + getName() + " Hours/wage: " + hoursWorked + "/" + wage;
	}

	public HourlyPaid() {
		//super("Lawson Joneschamp");
		super();
		hoursWorked = -1;
		wage = 0;
	}

	public HourlyPaid ( String name, int hoursWorked, double wage) {
		super ( name );
		this.hoursWorked = hoursWorked;
		this.wage = wage;
	}

	public void printCheck () {
		System.out.println(this);
		System.out.println("Gross Pay = $" + hoursWorked * wage);
	}
//	public HourlyPaid(int hoursWorked) {
//		super("Lawson JonesyChampy Lawless The Second");
//		this.hoursWorked = hoursWorked;
//	}

//	@Override
//	public void someMethod() {
//		System.out.println("Some stuff in the hourly paid class...");
//	}
//	public void someMethod(int dummy) {
//		super.someMethod();
//		System.out.println("Some stuff in the hourly paid class..." + dummy);
//	}

//	public int getHoursWorked() {
//		return hoursWorked;
//	}
//
//	public void setHoursWorked(int hoursWorked) {
//		this.hoursWorked = hoursWorked;
//	}


}

class SalaryPaid extends Employee {

//	public void abce () { //YOu cannot have an abc in the class if the abc() is static in Employee
//		System.out.println("I am from SalaryPaid...");
//	}

	private double salary;

	public double getSalary () {
		return salary;
	}

	public void setSalary (double salary) {
		this.salary = salary;
	}

	public SalaryPaid() {
		this.salary = 0;
	}

	public SalaryPaid(String name, double salary) {
		super(name);
		this.salary = salary;
	}

	@Override
	public void printCheck () {
		System.out.println(getName());
		System.out.println("Gross Pay $" + salary);
	}

	@Override
	public String toString() {
		return "S -->" + getName() + " Salary: " + salary;
	}

}

//________________________________
class Supervisor extends SalaryPaid {

//	public void abcd () {
//		//super.abc(); //this will run the abc from the Salary Paid class if the abc is not static otherwise it will run employees
//		//Employee.abc();
//		super.abce();
//		super.abc();
//	}

	private double bonus;

	public void setBonus (double bonus) {
		this.bonus = bonus;
	}

	public double getBonus () {
		return bonus;
	}

	public Supervisor () {
		bonus = 0;
	}

	public Supervisor ( String name, double salary, double bonus) {
		super ( name, salary);
		this.bonus = bonus;
	}

	@Override
	public String toString () {
		return "SP->" + getName() + "Salary = " + getSalary() + " Bonus = " + bonus + " Total yearly pay: " + (getSalary() + bonus);

	}

	@Override
	public void printCheck () {
		super.printCheck();
		System.out.println("Bonus = " + bonus);
	}
}
