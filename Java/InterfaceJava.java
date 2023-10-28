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
