public class Testeer {

	public static void main(String[] args) {
		Class cak = new Class();
		cak.printData();
		//Drivable driv = new Teenager(), cap, bik;
//		Drivable cap = new Plane();
//
//		if ( cap instanceof Plane) ((Plane)cap).planeThing();
//		else
//			System.out.println("Hold on! Only planes can do plane stuff GOT IT!?");
//		Drivable cap = new Teenager(); //if creating Teenager it cannot be converted to Vehicle and Plane because it has no connection to them
		//Drivable cap = new Plane(); //if creating Drivable cap you need (Vehicle) to convert and use the vehicle methods and data
		//Plane cap = new Plane();
		//cap.drive();
		//cap.wash(); //These two work becuase you are using the Plane class and not making it of interface Drivable or Washable who contain only one method each
//		((Vehicle)cap).setLength(200);
//		((Vehicle)cap).getLengthOfVehicle(); //THis will use the method of Vehicle
//		((Plane)cap).planeThing(); //You need to convert it to Plane if you want to use Plane methods.
		//bik = new Bike();
		//driv.drive();
		//cap.drive();
		//Washable washableCap = (Washable) cap;
		//washableCap.wash();
		//washableCap.drive();
		//cap.hello();
		//cap.wash();
		//bik.drive();


	}

}

interface Interface { //interfaces are classes with no code
	abstract public void method();
	final int data = 500; //final is a constant it applies to all data inside the interface whether you specify or not
}
class Class implements Interface {
	public void method() {
		System.out.println(" doing method inside class Class!");
	}

	public void printData() {
		//data = 700; //final data is not changeable at any point and interface data is ALWAYS FINAL!
		System.out.println(data);
	}
}
//interface Drivable { //interfaces can only have abstract methods
//	abstract public void drive();
//}
//
//interface Washable {
//	public void wash (); //abstract does not matter
//}
////_______________________
//class Teenager implements Drivable, Washable {
//
//	@Override
//	public void drive() {
//		System.out.println("Driving my parents crazy....");
//	}
//
//	@Override
//	public void wash() {
//		System.out.println("Smear in cologne");
//	}
//}
//abstract class Vehicle {
//	private int length = 0;
//
//	public int getLength() {
//		return length;
//	}
//
//	public void setLength(int length) {
//		this.length = length;
//	}
//
//	public void getLengthOfVehicle() {
//		System.out.println("Vehicle is this long: " + length);
//	}
//
////	public void drive() {
////		System.out.println("Driving a vehicle");
////	}
//}
////________________________
//class Plane extends Vehicle implements Drivable, Washable {
//
//	public void planeThing() {
//		System.out.println("Plane Thing");
//	}
//
//	@Override
//	public void drive() {
//		System.out.println("Driving the plane go wrrrrrrrr and brrrrrr and AAAAAHHHHH WE ARE GOING DOWN!");
//	}
//
//	@Override
//	public void wash() {
//		System.out.println("Too big to wash you must use a monster sized rag!!");
//	}
//
////	public Plane(int length) {
////		this.setLength(length);
////	}
//}
//
//class Bike implements Drivable, Washable {
//
//	@Override
//	public void drive() {
//		System.out.println("GET OUT OF THE BIKE LANE GOOOOD WHYYYY THE ROADS ARE CLOSED FOR THE CHILD MARCH!");
//	}
//
//	@Override
//	public void wash() {
//		System.out.println("Spray paint and small rags");
//	}
//}
