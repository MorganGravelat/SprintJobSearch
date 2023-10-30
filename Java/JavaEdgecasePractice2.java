/* Problem 9
interface P
{
	public void doNothing(); //interfaces only have constants and abstract methods anything implementing P must have doNothing()
}
*/

/*Problem 11
class KitchenAppliance {
	private String appName;
	private String appUse;

	public void setDetails(String appName, String appUse) {
		this.appName = appName;
		this.appUse = appUse;
	}

	public void printDetails() {
		System.out.print(appName+"|"+appUse+"|");
	}

	public void setPrice(double price) {
		price = 199.99;
	}
}
*/

public class Tester /*implements P for Problem 9*/ /*extends KitchenAppliance for Problem 11*/ {
	/*Problem 9
	public void doNothing() {
		System.out.print("abc");
	}
	*/
	/* Problem 11
	private double appPrice;

	public void setPrice(double appPrice) {
		this.appPrice = appPrice;
	}

	public void printDetails() {
		System.out.print(appPrice+"|");
	}
	*/
	/* Problem 17
	public static void checkingOn(Employee e1, Employee e2) {
		e1.work(e2);
	}
	*/
	public static void main(String[] args) {
		/*Problem 1
		Employee es = new Manager();
		es.work();
		*/
		/* Problem 2
		Employee es = new Manager(); // This will only have access to overrided methods
		//System.out.println(es.hours); //It does not have the variables
		//es.work(4); // es.work() won't work because it is an Employee class of type manager so it
		 */
		/*Problem 3
		Employee es = new Supervisor();

		es.work();

		System.out.println(" AND ");

		es = new Manager ();
		*/
		/* Problem 4
		Employee es = new Supervisor();
		Employee em = new Manager();
		Employee e = new Employee();

		e = em;
		em = es;
		es = e;

		es.work(); //Manager slacking off since it is class Employee of the manager object and hte work() is overrided
		*/
		/* Problem 5
		String [] names = new String[3];

		int i = 0;

		for ( String name: names) { //String name iterates through the loop as a read only variable
			//System.out.println(name);
			name = new String("S");
			names[i] = name;
			i++;
		}

		try {
			for (String name: names) //Loops through every iteration of the loop which is now { "S", "S", "S" }
				System.out.print(name); //Prints SSS into console and no error occurs
		}
		catch (Exception e) {
			System.out.println("E");
		}
		*/
		/* Problem 6
		Vehicle fastBoat = new Boat();
		fastBoat.print();
		*/
		/* Problem 7
		int a = 0, b = 3;
		int[] array = { 1, 2, 3 };

		try {
			System.out.println(array[b]); //There is no position 3 in the array so ArrayIndexOutOfBoundsException

			try {
				System.out.println( b / a ); //This is not a null pointer exception just a normal error	since you are doing 2 / 0 which is Arithmetic Exception
			} catch (NullPointerException npe) {
				System.out.print("A");
			}

		} catch (Exception e) { //Since error in the start B is printed
			System.out.print("B");
		} finally { //Finally is always printed
			System.out.print("C"); //PRINT BC
		}
		*/
		/* Problem 8
		Parent[] list = new Child[2];

		for (Parent p: list) { p = new Child(1,2); } // p is a temp variable so nothing changes for the actual array

		try {
			list[0].print(); //null.print is a null pointer exception and thus! AN EXCEPTION SO HAVE A NICE THANKSGIVING!!!!
			list[1].print();
		}
		catch (Exception e) { System.out.println("Have a nice Thanksgiving!"); }
		*/

		/* Problem 9
		doNothing(0); //Runs the doNothing(int)
		*/
		/* Problem 10
		MyAbstract obj = new MyClass();
		obj.print(5); //The method sets this.i to 6 but then prints the argument number 5
		*/
		/*Problem 11
		KitchenAppliance mxCompany = new Tester();
		mxCompany.setDetails("Blender", "blends food");
		mxCompany.setPrice(145.99); //This is overrided in the Tester class so the method will be used within the Tester Object
		mxCompany.printDetails(); // This overrided method is the price 145.99 + | so 145.99|
		*/
		/*Problem 12
		Boat fastBoat = new Boat(2); //The constructor sets numEgines to 2
		fastBoat.setName("Firebird"); //This name is applied via the method from the vehicle class
		System.out.print(fastBoat); //This invokes the toString which returns vehicle name Firebird and adds the num of engines after a space
		*/
		/*Problem 13
		Vehicle vb = new Boat(); // Boat has no constructor so it uses the default constructor provided by Java
		System.out.print(vb); //The toString prints out "Boat for " and then the doingSomething interface method prints "boating"
		vb.doingSomething(); //So the two prints give Boat for boating
		*/
		/*Problem 14
		Vehicle vb = new Boat();
		System.out.print(vb); //toString is going to print "Boat for "
		vb.doingSomething(); // doingSomething overidded to print "sail sail" so "Boat for sail sail"
		*/
		/* Problem 15
		Parent p = new Child (1,2);
		p.print();
		*/
		/* Problem 16
		try {
			System.out.print("In try: ");
			throw new MyException();
		} catch (MyException me) { //This catch will activate since you created a new exception
			System.out.print(me.getMessage());
		} catch (Exception e) { //This will not proc since the first one did
			System.out.print("Ah!");
		} finally { //Finally always fires off
			System.out.print("Regardless");
		}
		*/
		/* Problem 17
		Employee e = new Employee();
		Manager m = new Manager();
		Employee em = new Manager();

		checkingOn(e, m); //No matter what e.work() will print A when a manager or employee is put in since it is all extended from emp.
		*/
		/* Problem 18
		Employee m = new Manager(50);
		Employee s = new Supervisor();

		m = s;

		m.work();
		*/
		/* Problem 19
		Manager m = new Manager(50);
		Employee e = new Manager(100);

		System.out.print(m.type() + " and ");
		e.work(50);
		*/

		/* Problem 20
		String[] names = new String[2];

		int i = 0;

		for (String name : names) {
			name = new String("1");
			names[i] = name;
			i++;
		}

		try {
			for (String name : names)
				System.out.print(name);

			throw new NullPointerException();
		} catch (Exception e) {
			System.out.print("ERROR");
		} finally {
			System.out.print("A");
		}
		*/
		/* Problem 21
		int a = 0, b = 3;

		try {
			try {
				System.out.println(b / a); //this will throw an arithmetic exception so the null pointer wont catch it
			} catch (NullPointerException npe) {
				System.out.print("A");
			}
			finally { //prints B
				System.out.print("B");
			}
		} catch (Exception e) { //Since it didn't catch in the first try statement it will catch here
			System.out.print("C"); //So C will print
		} finally {
			System.out.print("D"); //In the end it will be BCD in the console
		}
		*/
		///* Problem 22
		A aObject = new C();
		System.out.println(aObject);
		//*/

	}
	/*Problem 9
	public static void doNothing( int dammy ) {
		(new Tester()).doNothing(); //Runs the doNothing() method of Tester "abc"
		System.out.print("xyz"); //prints xyz so it will be "abcxyz"
	}
	*/
}
/* Problem 1
class Employee {
	public void work() { System.out.println("Employee working hard!"); }

}

class Manager extends Employee {

	public void work() { System.out.print("Manager slacking off!"); }
}
*/
/* Problem 2
class Employee {
	public void work() { System.out.println("Employee working hard!"); }

}
class Manager extends Employee {
	public int hours = 10;
	public void work(int hours) { System.out.print("Manager slept for " + hours); }
}
*/
/* Problem 3
class Employee {
	public void work() { System.out.println("Employee working hard!"); }
}

class Manager extends Employee {

	public void work() { System.out.print("Manager slacking off!"); }
}

class Supervisor extends Employee {
	public void work() { System.out.print("Supervisor taking a nap!"); }
}
*/
/* Problem 4
class Employee {
	public void work() { System.out.println("Employee working hard!"); }
}

class Manager extends Employee {

	public void work() { System.out.print("Manager slacking off!");}
}

class Supervisor extends Manager {
	public void work() { System.out.print("Supervisor taking a nap!"); }
}
*/
/* Problem 6
class Vehicle {
	public int print() {
		System.out.print("Vehicle");
		return 0;
	}
}

class Boat extends Vehicle {
	public void print(int i) {
		System.out.print("Boat");
	}
}
*/
/* Problem 8
abstract class Parent {
	private int x;
	public Parent(int x) { this.x = x; }
	public abstract void print();
}

class Child extends Parent {
	private int y;

	public Child(int x, int y) {
		super(x);
		this.y = y;
	}

	public void print() {
		System.out.print(y);
	}
}
*/
/*Problem 10
abstract class MyAbstract {
	public int i;
	public void print(int i) {
		this.i = 6;
		System.out.println(i);
	}
}

class MyClass extends MyAbstract {
	public void print() {
		i = 5;
		System.out.println(this.i);
	}

	public MyClass() {
		i = 4;
	}
}
*/
/* Problem 12
class Vehicle {
	private String vehicleName;

	public void setName (String name) {
		vehicleName = name;
	}

	public String toString() {
		return vehicleName;
	}
}

class Boat extends Vehicle {
	private int numEngines;

	public Boat(int num) {
		numEngines = num;
	}

	public String toString() {
		return super.toString() + " " + numEngines;
	}
}
*/
/*Problem 13
interface Thing {
	public void doingSomething();
}

abstract class Vehicle implements Thing {

	@Override
	public String toString () {
		return "Vehicle for ";
	}
}

class Boat extends Vehicle {

	@Override
	public String toString () {
		return "Boat for ";
	}
	@Override
	public void doingSomething() {
		System.out.print("boating");
	}
}
*/
/*
interface Thing {
	public void doingSomething();
}

abstract class Vehicle implements Thing {

	@Override
	public void doingSomething() {
		System.out.print("vroom vroom");
	}
	@Override
	public String toString () {
		return "Vehicle for ";
	}
}

class Boat extends Vehicle implements Thing {

	@Override
	public void doingSomething() {
		System.out.print("sail sail");
	}

	@Override
	public String toString () {
		return "Boat for ";
	}
}
*/

/*
abstract class Parent {
	private int x;

	public void setX(int x) {
		this.x = x;
	}
	public Parent(int x) {
		this.x = x;
	}

	public abstract void print();
}

class Child extends Parent {
	private int y;
	public Child(int x, int y) { //This chains the constructor of Parent as well and will require a super(x) call to function
		setX(x); //This will not work because there is no default Parent() constructor you need to call super(x)
	}

	public void print() {
		System.out.print(y);
	}
}
*/
/*Problem 16
class MyException extends Exception {
	public String getMessage() {
		return "My Bad!";
	}
}
*/
/* Problem 17
class Employee {
	public void work(Employee e) { //manager extends employee so it still counts asn an Employee e when it is in work();
		System.out.print("A");
	}
	public void work(Manager m) {
		System.out.print("B");
	}
}

class Manager extends Employee {

	public void work(Employee e) {
		System.out.print("C");
	}
}
*/
/* Problem 18
abstract class Employee {
	public abstract void work();
}

class Manager extends Employee {
	private double salary;

	public void work() { salary = 0; }

	public Manager(double salary) { this.salary = salary;}

	public void work(double salary) { System.out.print("M" + salary);}

}

class Supervisor extends Manager {
	public Supervisor() { super(100); }

	public void work() { System.out.print("S"); }
}
*/
/* Problem 19
interface Person {
	public String type();
}

abstract class Employee implements Person {
	public void work(int salary) { System.out.print("M" + salary);}
	public abstract void work();
}

class Manager extends Employee {

	public int salary;

	public String type() { return "Manager";}

	public void work() { salary = 0; }

	public Manager(int salary) { this.salary = salary; }

	public void work(int salary) { System.out.print("M" + salary);}
}
*/

/*Problem 22
class A {

}
class B extends A {
	public String toString() {
		return super.toString() + "A";
	}
}

class C extends B {
	public String toString() {
		return "C";
	}
}
*/
