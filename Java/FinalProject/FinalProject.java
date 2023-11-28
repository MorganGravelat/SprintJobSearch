import java.util.*;

public class FinalProject {

	public static void main(String[] args) {


	}

}


abstract class Person {
	private String fullName;
	private String id;

	public Person(String fullName, String id) {
		this.fullName = fullName;
		this.id = id;
	}

	public Person(String id) {
		fullName = "No Name";
		this.id = id;
	}

	public abstract void print();

	public String getFullName() {
		return fullName;
	}

	public void setFullName(String fullName) {
		this.fullName = fullName;
	}

	public String getId() {
		return id;
	}

	public void setId(String id) {
		this.id = id;
	}

}

class Student extends Person {
	private double gpa;
	private int creditHours;

	public Student(String fullName, String id, double gpa, int creditHours) {
		super(fullName, id);
		this.gpa = gpa;
		this.creditHours = creditHours;
	}
	public Student(String id, double gpa, int creditHours) {
		super(id);
		this.gpa = gpa;
		this.creditHours = creditHours;
	}

	public void print() {
		System.out.println("Student Invoice:");
		System.out.println("ID: " this.getId() + ", Name: " + this.getFullName() + ", GPA: " + gpa);
		System.out.println("Tuition: " + calculateTuition());
	}

	private double calculateTuition() {
		double baseTuition = creditHours > 0 ? 236.45 * creditHours + 52 : 0;
		return gpa >= 3.85 ? baseTuition * 0.75 : baseTuition;
	}
	public double getGpa() {
		return gpa;
	}
	public void setGpa(double gpa) {
		this.gpa = gpa;
	}
	public int getCreditHours() {
		return creditHours;
	}
	public void setCreditHours(int creditHours) {
		this.creditHours = creditHours;
	}

}
