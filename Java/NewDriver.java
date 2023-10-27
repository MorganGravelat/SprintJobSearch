import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

public class Driver {

	public static void main(String[] args) {
		ArrayList <Employee> list = new ArrayList<Employee> ();

		list.add(new Employee("Sam", 111));
		list.add(new Employee("Kim", 555));
		list.add(new Employee("Jen", 333));
		list.add(new Employee("Jac", 222));

		System.out.println("Before Sorting ....\n");
		for ( Employee e: list)
			System.out.println(e);

		//Lets sort Jessie
		Collections.sort(list);

		System.out.println("\n______________\n\n\nAfter Sorting ....\n");
		for ( Employee e: list)
			System.out.println(e);

//		Employee emp1 = new Employee ( "Sam" , 1111);
//		Employee emp2 = new Employee ( "Erika" , 2222);
//
//		System.out.println(emp1.compareTo(emp2));

//		double [] array = { 12, 52, 15, 60, 100, -1, 45 };
//
//		System.out.println("Before....");
//		for ( double a: array)
//			System.out.println(a+"\t");
//
//		System.out.println("_________________________");
//		Arrays.sort(array);
//		System.out.println("After....");
//		for ( double a: array)
//			System.out.println(a+"\t");
//		String [] array = { "12", "52", "15", "60", "100", "-1", "45" };
//
//		//System.out.println((int)'!' + " " + (int)'1');//ASCII code is provided when you convert to int
//
//		System.out.println("Before....");
//		for ( String a: array)
//			System.out.println(a+"\t");
//
//		System.out.println("_________________________");
//		Arrays.sort(array);
//		System.out.println("After....");
//		for ( String a: array)
//			System.out.println(a+"\t");

	}

}
//__________________
class Employee implements Comparable<Employee>{
	public String name;
	public int id;

	public Employee ( String name, int id) {
		this.name = name;
		this.id = id;
	}
	public String toString() {
		return name + "/" + id;
	}
/*
	@Override
	public int compareTo(Employee o) {

//		if (this.id == o.id)
//			return 0;
//		else if ( this.id > o.id ) return 1;
//
//		return -1;
		return this.id - o.id; //this will ascend the sort 111/222/333/555
		//return -this.id + o.id; This will descend the sort 555/333/222/111

	}
	*/
	public int compareTo ( Employee o) {
		//return name.compareTo(o.name);
		return name.indexOf(0).compareTo(o.name.indexOf(0));
	}
}
