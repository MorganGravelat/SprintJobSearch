import java.util.*;
import java.io.*;
import java.time.LocalDate;

public class FinalProject {

	private static int peopleCount = 0;
	private static int MAX_PEOPLE = 100;

	public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        Person[] people = new Person[MAX_PEOPLE];
        boolean exit = false;
        System.out.println("Welcome to my Personal Management Program");
        while (!exit) {
        	int choice = 0;
            System.out.println("Choose one of the options:");
            System.out.println("1- Enter the information of a faculty");
            System.out.println("2- Enter the information of a student");
            System.out.println("3- Print tuition invoice for a student");
            System.out.println("4- Print faculty information");
            System.out.println("5- Enter the information of a staff member");
            System.out.println("6- Print the information of a staff member");
            System.out.println("7- Delete a person");
            System.out.println("8- Exit Program");
            System.out.print("\n\tEnter your selection: ");

            try {
                choice = Integer.parseInt(scanner.nextLine());
            } catch (NumberFormatException e) {
                System.out.println("\nInvalid entry- please enter a number.\n");
                continue;
            }
            //scanner.nextLine(); // consume the remaining newline

            switch (choice) {
            case 1:
                if (peopleCount < MAX_PEOPLE) {
                    addFaculty(scanner, people);
                } else {
                    System.out.println("Maximum capacity reached, cannot add more persons.");
                }
                break;
            case 2:
                if (peopleCount < MAX_PEOPLE) {
                    addStudent(scanner, people);
                } else {
                    System.out.println("Maximum capacity reached, cannot add more persons.");
                }
                break;
            case 3:
                printStudentInvoice(scanner, people);
                break;
            case 4:
                printFacultyInformation(scanner, people);
                break;
            case 5:
                if (peopleCount < MAX_PEOPLE) {
                    addStaff(scanner, people);
                } else {
                    System.out.println("Maximum capacity reached, cannot add more persons.");
                }
                break;
            case 6:
                printStaffInformation(scanner, people);
                break;
            case 7:
                deletePerson(scanner, people);
                break;
            case 8:
                exitProgram(scanner, people);
                exit = true;
                break;
            default:
                System.out.println("Invalid entry- please try again");
            }
        }
        scanner.close();
    }

	private static void addStudent(Scanner scanner, Person[] people) {
	    System.out.println("Enter the student info:");

	    System.out.print("\tName of Student: ");
	    String name = scanner.nextLine();

	    String id = getValidId(scanner, people);

	    double gpa = 0;
	    do {
	        System.out.print("\tGpa: ");
	        try {
	            gpa = Double.parseDouble(scanner.nextLine());
	        } catch (NumberFormatException e) {
	            System.out.println("Invalid input. Please enter a number for GPA.");
	            continue; // continue the loop for another attempt
	        }
	        //scanner.nextLine(); // consume the newline character
	    } while (gpa < 0.0 || gpa > 4.0); // assuming GPA is between 0.0 and 4.0
	    //System.out.println(gpa);

	    int creditHours;
	    do {
	        System.out.print("\tCredit hours: ");
	        while (!scanner.hasNextInt()) {
	            System.out.println("Invalid input. Please enter an integer for credit hours.");
	            System.out.print("Credit hours: ");
	            scanner.next(); // consume the invalid input
	        }
	        creditHours = scanner.nextInt();
	    } while (creditHours < 0);

	    scanner.nextLine(); // consume the remaining newline

	    people[peopleCount++] = new Student(name, id, gpa, creditHours);
	    System.out.println("Student added!\n\n");
	}

	private static void addFaculty(Scanner scanner, Person[] people) {
	    System.out.println("Enter the faculty info:");

	    System.out.print("Name of the faculty: ");
	    String name = scanner.nextLine();

	    String id = getValidId(scanner, people);

	    String department = getValidDepartment(scanner, people);

	    String rank;
	    do {
	        System.out.print("Rank (Professor/Adjunct): ");
	        rank = scanner.nextLine();
	        rank = rank.toLowerCase();
	        System.out.println(rank);
	        if (!isValidRank(rank)) {
	            System.out.println("Invalid rank. Please enter 'Professor' or 'Adjunct'.");
	        }
	    } while (!isValidRank(rank));



	    people[peopleCount++] = new Faculty(name, id, department, rank);
	    System.out.println("Faculty added!");
	}

	private static void addStaff(Scanner scanner, Person[] people) {
	    System.out.println("Enter the staff info:");

	    System.out.print("Name of the staff member: ");
	    String name = scanner.nextLine();

	    String id = getValidId(scanner, people);

	    String department = getValidDepartment(scanner, people);

	    String status;
	    do {
	        System.out.print("Status, Enter P for Part Time, or Enter F for Full Time: ");
	        status = scanner.nextLine().toUpperCase();
	    } while (!status.equals("P") && !status.equals("F"));

	    String fullStatus = status.equals("P") ? "Part Time" : "Full Time";

	    people[peopleCount++] = new Staff(name, id, department, fullStatus);
	    System.out.println("Staff member added!");
	}

	private static String getValidId(Scanner scanner, Person[] people) {
		String id;
		do {
	        System.out.print("\tID: ");
	        id = scanner.nextLine();
	        if (!isValidId(id)) {
	            System.out.println("\tInvalid ID format. Must be LetterLetterDigitDigitDigitDigit.");
	        } else if (isDuplicateId(id, people)) {
	            System.out.println("\tID already exists. Please enter a different ID.");
	        }
	    } while (!isValidId(id) || isDuplicateId(id, people));

		return id;
	}

	private static String getValidDepartment(Scanner scanner, Person[] people) {

		String department;
	    do {
	        System.out.print("Department (Mathematics/Engineering/English): ");
	        department = scanner.nextLine();
	        department = department.toLowerCase();
	        if (!isValidDepartment(department)) {
	            System.out.println("Invalid department. Please enter a valid department.");
	        }
	    } while (!isValidDepartment(department));

		return department;
	}

	private static void deletePerson(Scanner scanner, Person[] people) {
	    System.out.print("Enter the id of the person to delete: ");
	    String id = scanner.nextLine();

	    boolean found = false;
	    for (int i = 0; i < peopleCount; i++) {
	        if (people[i].getId().equalsIgnoreCase(id)) {
	            found = true;
	            // Shift all subsequent elements to the left
	            for (int j = i; j < peopleCount - 1; j++) {
	                people[j] = people[j + 1];
	            }
	            peopleCount--; // Decrease the count of people
	            people[peopleCount] = null; // Nullify the last element
	            System.out.println("Person with ID " + id + " has been deleted.");
	            break;
	        }
	    }

	    if (!found) {
	        System.out.println("Sorry, no such person exists.");
	    }
	}



    private static void printStudentInvoice(Scanner scanner, Person[] people) {
	    System.out.print("Enter the student's ID: ");
	    String id = scanner.nextLine();

	    boolean found = false;
	    for (int i = 0; i < peopleCount; i++) {
	        if (people[i] instanceof Student && people[i].getId().equalsIgnoreCase(id)) {
	            ((Student) people[i]).print(); // Print the student's invoice
	            found = true;
	            break;
	        }
	    }

	    if (!found) {
	        System.out.println("No student matched!");
	    }
	}

	private static void printFacultyInformation(Scanner scanner, Person[] people) {
	    System.out.print("Enter the Faculty's ID: ");
	    String id = scanner.nextLine();

	    boolean found = false;
	    for (int i = 0; i < peopleCount; i++) {
	        if (people[i] instanceof Faculty && people[i].getId().equalsIgnoreCase(id)) {
	            people[i].print(); // Call the print method of the Faculty class
	            found = true;
	            break;
	        }
	    }

	    if (!found) {
	        System.out.println("No faculty member matched!");
	    }
	}

	private static void printStaffInformation(Scanner scanner, Person[] people) {
	    System.out.print("Enter the Staff's ID: ");
	    String id = scanner.nextLine();

	    boolean found = false;
	    for (int i = 0; i < peopleCount; i++) {
	        if (people[i] instanceof Staff && people[i].getId().equalsIgnoreCase(id)) {
	            people[i].print(); // Call the print method of the Staff class
	            found = true;
	            break;
	        }
	    }

	    if (!found) {
	        System.out.println("No staff member matched!");
	    }
	}a

    private static boolean isValidId(String id) {
	    return id.matches("[a-zA-Z]{2}\\d{4}");
	}

	private static boolean isDuplicateId(String id, Person[] people) {
	    for (int i = 0; i < peopleCount; i++) {
	        if (people[i].getId().equalsIgnoreCase(id)) {
	            return true;
	        }
	    }
	    return false;
	}

	private static boolean isValidDepartment(String department) {
	    String[] validDepartments = {"Mathematics", "Engineering", "English"};
	    for (String validDept : validDepartments) {
	        if (validDept.equalsIgnoreCase(department)) {
	            return true;
	        }
	    }
	    return false;
	}

}


abstract class Person { //Person
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

    @Override
	public void print() {
	    double tuitionPerCreditHour = 236.45;
	    double fees = 52;
	    double totalTuition = calculateTuition();
	    double discount = (creditHours > 0 ? 236.45 * creditHours + 52 : 0) - totalTuition;

	    System.out.println("---------------------------------------------------------------------------");
	    System.out.println(this.getFullName() + " " + this.getId());
	    System.out.println("Credit Hours: " + creditHours + " ($" + tuitionPerCreditHour + "/credit hour)");
	    System.out.println("Fees: $" + fees);
	    System.out.println("Total payment (after discount): $" + String.format("%.2f", totalTuition) + " ($" + String.format("%.2f", discount) + " discount applied)");
	    System.out.println("---------------------------------------------------------------------------");
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

abstract class Employee extends Person {
	private String department;

	public Employee(String fullName, String id, String department) {
		super(fullName, id);
		this.department = department;
	}

	public Employee(String id, String department) {
		super(id);
		this.department = department;
	}

	public String getDepartment() {
		return department;
	}

	public void setDepartment(String department) {
		this.department = department;
	}
}

class Faculty extends Employee {
	private String rank;

	public Faculty(String fullName, String id, String department, String rank) {
		super(fullName, id , department);
		this.rank = rank;
	}

	public Faculty(String id, String department, String rank) {
		super(id , department);
		this.rank = rank;
	}

    @Override
    public void print() {
        System.out.println("---------------------------------------------------------------------------");
        System.out.println(this.getFullName() + " " + this.getId());
        System.out.println(this.getDepartment() + " Department, " + rank);
        System.out.println("---------------------------------------------------------------------------");
    }

	public String getRank() {
		return rank;
	}

	public void setRank(String rank) {
		this.rank = rank;
	}


}

class Staff extends Employee {
	private String status;

	public Staff(String fullName, String id, String department, String status) {
		super(fullName, id, department);
		this.status = status;
	}
	public Staff(String id, String department, String status) {
		super(id, department);
		this.status = status;
	}

	 @Override
	 public void print() {
	     System.out.println("---------------------------------------------------------------------------");
	     System.out.println(this.getFullName() + " " + this.getId());
	     System.out.println(this.getDepartment() + " Department, " + (status.equals("F") ? "Full Time" : "Part Time"));
	     System.out.println("---------------------------------------------------------------------------");
	 }

	public String getStatus() {
		return status;
	}

	public void setStatus(String status) {
		this.status = status;
	}
}
