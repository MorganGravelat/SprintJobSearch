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
        System.out.println("\t\t\tWelcome to my Personal Management Program\n\n");
        System.out.println("Choose one of the options:\n");
        while (!exit) {
        	int choice = 0;
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
                System.out.println("\nInvalid entry- please try again.\n\n");
                continue;
            }

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
                printStudent(scanner, people);
                break;
            case 4:
                printFaculty(scanner, people);
                break;
            case 5:
                if (peopleCount < MAX_PEOPLE) {
                    addStaff(scanner, people);
                } else {
                    System.out.println("Maximum capacity reached, cannot add more persons.");
                }
                break;
            case 6:
                printStaff(scanner, people);
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
	    System.out.println("\n\nEnter the student info:");

	    System.out.print("\tName of Student (or NA to leave it blank): ");
	    String name = scanner.nextLine();

	    if ("NA".equalsIgnoreCase(name)) {
	    	name = null;
	    }

	    String id = getValidId(scanner, people);

	    double gpa = 0;
	    boolean goodGpa = false;
	    do {
	        System.out.print("\tGpa: ");
	        try {
	            gpa = Double.parseDouble(scanner.nextLine());
	            if (gpa >= 0.0 && gpa <= 4.0) {
	                gpa = Double.parseDouble(String.format("%.2f", gpa));
	                goodGpa = true;
	            } else {
	                System.out.println("\tGPA must be between 0.0 and 4.0.");
	                continue;
	            }
	        } catch (NumberFormatException e) {
	            System.out.println("\tInvalid input. Please enter a number for GPA.");
	            continue;
	        }
	    } while (!goodGpa);

	    int creditHours;
	    do {
	        System.out.print("\tCredit hours: ");
	        while (!scanner.hasNextInt()) {
	            System.out.println("Invalid input. Please enter an integer for credit hours.");
	            System.out.print("\tCredit hours: ");
	            scanner.next();
	        }
	        creditHours = scanner.nextInt();
	    } while (creditHours < 0);

	    scanner.nextLine();

	    if (name == null) {
	    	people[peopleCount++] = new Student(id, gpa, creditHours);
	    } else {
	    	people[peopleCount++] = new Student(name, id, gpa, creditHours);
	    }
	    System.out.println("Student added!\n\n");
	}

	private static void addFaculty(Scanner scanner, Person[] people) {
	    System.out.println("\n\nEnter the faculty info:");

	    System.out.print("\tName of the faculty (or NA to leave it blank): ");
	    String name = scanner.nextLine();

	    if ("NA".equalsIgnoreCase(name)) {
	    	name = null;
	    }

	    String id = getValidId(scanner, people);



	    String rank;
	    do {
	        System.out.print("\n\tRank (Professor/Adjunct): ");
	        rank = scanner.nextLine();
	        rank = rank.toLowerCase();
	        if (!isValidRank(rank)) {
	            System.out.println("\t\t\"" + capitalizeFirstLetter(rank) + "\"" + " is invalid");
	        }
	    } while (!isValidRank(rank));

	    String department = getValidDepartment(scanner, people);

	    if (name == null) {
	    	people[peopleCount++] = new Faculty(id, capitalizeFirstLetter(department), capitalizeFirstLetter(rank));
	    } else {
	    	people[peopleCount++] = new Faculty(name, id, capitalizeFirstLetter(department), capitalizeFirstLetter(rank));
	    }

	    System.out.println("\nFaculty added!\n\n");
	}

	private static void addStaff(Scanner scanner, Person[] people) {
	    System.out.println("\nEnter the staff info:");

	    System.out.print("\tName of the staff member (or NA to leave it blank): ");
	    String name = scanner.nextLine();

	    if ("NA".equalsIgnoreCase(name)) {
	    	name = null;
	    }

	    String id = getValidId(scanner, people);

	    String department = getValidDepartment(scanner, people);

	    String status;
	    do {
	        System.out.print("\tStatus, Enter P for Part Time, or Enter F for Full Time: ");
	        status = scanner.nextLine().toUpperCase();
	    } while (!status.equals("P") && !status.equals("F"));
	    String fullStatus = status.equals("P") ? "Part Time" : "Full Time";
	    if (name == null) {
	    	people[peopleCount++] = new Staff(id, capitalizeFirstLetter(department), fullStatus);
	    } else {
	    	people[peopleCount++] = new Staff(name, id, capitalizeFirstLetter(department), fullStatus);
	    }

	    System.out.println("\nStaff member added!\n");
	}


	private static String getValidId(Scanner scanner, Person[] people) {
		String id;
		do {
	        System.out.print("\tID: ");
	        id = scanner.nextLine();
	        if (!isValidId(id)) {
	            System.out.println("\tInvalid ID format. Must be LetterLetterDigitDigitDigitDigit.\n");
	        } else if (isDuplicateId(id, people)) {
	            System.out.println("\tID already exists. Please enter a different ID.");
	        }
	    } while (!isValidId(id) || isDuplicateId(id, people));

	    id = id.substring(0, 2).toLowerCase() + id.substring(2);

		return id;
	}

	private static boolean isValidId(String id) {
	    return id.matches("[a-zA-Z]{2}\\d{4}");
	}

	private static String getValidDepartment(Scanner scanner, Person[] people) {

		String department;
	    do {
	        System.out.print("\tDepartment (Mathematics/Engineering/English): ");
	        department = scanner.nextLine();
	        department = department.toLowerCase();
	        if (!isValidDepartment(department)) {
	            System.out.println("Invalid department. Please enter a valid department.");
	        }
	    } while (!isValidDepartment(department));

		return department;
	}

	private static void deletePerson(Scanner scanner, Person[] people) {
	    System.out.print("\tEnter the id of the person to delete: ");
	    String id = scanner.nextLine();

	    boolean found = false;
	    for (int i = 0; i < peopleCount; i++) {
	        if (people[i].getId().equalsIgnoreCase(id)) {
	            found = true;
	            for (int j = i; j < peopleCount - 1; j++) {
	                people[j] = people[j + 1];
	            }
	            peopleCount--;
	            people[peopleCount] = null;
	            System.out.println("\nPerson with ID " + id + " has been deleted.\n\n");
	            break;
	        }
	    }

	    if (!found) {
	        System.out.println("\nSorry, no such person exists.\n\n");
	    }
	}

	private static void printStudent(Scanner scanner, Person[] people) {
	    System.out.print("\n\tEnter the student's ID: ");
	    String id = scanner.nextLine();

	    boolean found = false;
	    for (int i = 0; i < peopleCount; i++) {
	        if (people[i] instanceof Student && people[i].getId().equalsIgnoreCase(id)) {
	        	System.out.println("\n\tHere is the tuition invoice for " + people[i].getFullName() + "\n");
	            ((Student) people[i]).print();
	            found = true;
	            break;
	        }
	    }

	    if (!found) {
	        System.out.println("\tNo student matched!\n");
	    }
	}

	private static void printFaculty(Scanner scanner, Person[] people) {
	    System.out.print("\tEnter the Faculty's ID: ");
	    String id = scanner.nextLine();

	    boolean found = false;
	    for (int i = 0; i < peopleCount; i++) {
	        if (people[i] instanceof Faculty && people[i].getId().equalsIgnoreCase(id)) {
	            people[i].print();
	            found = true;
	            break;
	        }
	    }

	    if (!found) {
	        System.out.println("No faculty member matched!");
	    }
	}

	private static void printStaff(Scanner scanner, Person[] people) {
	    System.out.print("\n\tEnter the Staff's ID: ");
	    String id = scanner.nextLine();

	    boolean found = false;
	    for (int i = 0; i < peopleCount; i++) {
	        if (people[i] instanceof Staff && people[i].getId().equalsIgnoreCase(id)) {
	            people[i].print();
	            found = true;
	            break;
	        }
	    }

	    if (!found) {
	        System.out.println("\tNo staff member matched!\n");
	    }
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
	    String[] validDepartments = {"mathematics", "engineering", "english"};
	    for (String validDept : validDepartments) {
	        if (validDept.equalsIgnoreCase(department)) {
	            return true;
	        }
	    }
	    return false;
	}

	private static boolean isValidRank(String rank) {
	    String[] validRanks = {"professor", "adjunct"};
	    return Arrays.asList(validRanks).contains(rank);
	}

	public static String capitalizeFirstLetter(String str) {
	    if (str == null || str.isEmpty()) {
	        return str;
	    }

	    String[] words = str.split(" ");
	    StringBuilder capitalizedString = new StringBuilder();

	    for (String word : words) {
	        String capitalizedWord = word.substring(0, 1).toUpperCase() + word.substring(1);
	        capitalizedString.append(capitalizedWord).append(" ");
	    }

	    return capitalizedString.toString().trim();
	}

	private static void exitProgram(Scanner scanner, Person[] people) {
	    String choice = "";
	    do {
	    	System.out.print("Would you like to create the report? (Y/N): ");
	    	choice = scanner.nextLine();
		    if (choice.equalsIgnoreCase("Y")) {
		        int sortChoice = 0;
		        boolean validInput = false;
		        while (!validInput) {
		            System.out.print("Would you like to sort your students by descending gpa or name (1 for gpa, 2 for name): ");
		            try {
		                sortChoice = scanner.nextInt();
		                scanner.nextLine();
		                if (sortChoice == 1 || sortChoice == 2) {
		                    validInput = true;
		                } else {
		                    System.out.println("Please enter 1 for GPA or 2 for name.");
		                }
		            } catch (InputMismatchException e) {
		                System.out.println("Invalid entry. Please enter 1 for GPA or 2 for name.");
		            }
		        }

		        sortStudents(people, sortChoice);
		        generateReport(people, sortChoice);
		    } else if (choice.equalsIgnoreCase("N")) {
		    	System.out.println("Goodbye!");
		    	break;
		    } else {
		    	System.out.println("\nInvalid choice type Y for yes or N for no");
		    }
	    }while (!choice.equalsIgnoreCase("Y") && !choice.equalsIgnoreCase("N"));
	}

    private static void sortStudents(Person[] people, int sortChoice) {
        Arrays.sort(people, 0, peopleCount, new Comparator<Person>() {
            @Override
            public int compare(Person p1, Person p2) {
                if (p1 instanceof Student && p2 instanceof Student) {
                    Student s1 = (Student) p1;
                    Student s2 = (Student) p2;
                    if (sortChoice == 1) {
                        return Double.compare(s2.getGpa(), s1.getGpa());
                    } else {
                        return s1.getFullName().compareToIgnoreCase(s2.getFullName());
                    }
                }
                return 0;
            }
        });
    }

    private static void generateReport(Person[] people, int sortChoice) {
        try (PrintWriter writer = new PrintWriter(new File("report.txt"))) {
            writer.println("Report created on " + LocalDate.now());
            writer.println("***********************\n");

            writer.println("Faculty Members");
            writer.println("----------------");
            int count = 1;
            for (Person p : people) {
                if (p instanceof Faculty) {
                	if(count > 1) {
                        writer.println("\n\t"+count++ + ". " + p.getFullName());
                	} else {
                        writer.println("\t"+count++ + ". " + p.getFullName());
                	}
                    writer.println("\t"+"ID: " + p.getId());
                    writer.println("\t"+((Faculty) p).getRank() + "," + ((Faculty) p).getDepartment());
                }
            }

            writer.println("\n\nStaff Members");
            writer.println("----------------");
            count = 1;
            for (Person p : people) {
                if (p instanceof Staff) {
                	if(count > 1) {
                        writer.println("\n\t"+count++ + ". " + p.getFullName());
                	} else {
                        writer.println("\t"+count++ + ". " + p.getFullName());
                	}
                    writer.println("\t"+"ID: " + p.getId());
                    writer.println("\t"+((Staff) p).getDepartment() + ", " + ((Staff) p).getStatus());
                }
            }

            writer.println("\n\nStudents");
            writer.println("---------");
            count = 1;
            for (Person p : people) {
                if (p instanceof Student) {
                	if(count > 1) {
                        writer.println("\n\t"+count++ + ". " + p.getFullName());
                	} else {
                        writer.println("\t"+count++ + ". " + p.getFullName());
                	}
                    writer.println("\t"+"ID: " + p.getId());
                    writer.println("\t"+"Gpa: " + ((Student) p).getGpa());
                    writer.println("\t"+"Credit hours: " + ((Student) p).getCreditHours());
                }
            }
            System.out.println("Report created and saved on your hard drive!");
	    	System.out.println("Goodbye!");
        } catch (FileNotFoundException e) {
            System.out.println("An error occurred while creating the report.");
        }
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

    @Override
    public void print() {
        double totalTuition = calculateTuition();
        double discount = (creditHours > 0 ? 236.45 * creditHours + 52 : 0) - totalTuition;

        System.out.println("---------------------------------------------------------------------------");
        System.out.println(this.getFullName() + " \t\t" + this.getId());
        System.out.println("\nCredit Hours:" + creditHours + " (236.45/credit hour)");
        System.out.println("\nFees: $52");
        System.out.println("\nTotal payment (after discount): $" + formatDollarAmount(totalTuition) + " \t($" + formatDollarAmount(discount) + " discount applied)");
        System.out.println("---------------------------------------------------------------------------\n\n");
    }

    private String formatDollarAmount(double amount) {
        if (amount == (long) amount) {
            return String.format("%d", (long) amount);
        } else {
            return String.format("%.2f", amount);
        }
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
        System.out.println("\n---------------------------------------------------------------------------");
        System.out.println(this.getFullName() + " \t\t" + this.getId());
        System.out.println("\n"+this.getDepartment() + " Department, " + rank);
        System.out.println("---------------------------------------------------------------------------\n");
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
	     System.out.println(this.getFullName() + " \t" + this.getId());
	     System.out.println("\n"+this.getDepartment() + " Department, " + status);
	     System.out.println("---------------------------------------------------------------------------");
	 }

	public String getStatus() {
		return status;
	}

	public void setStatus(String status) {
		this.status = status;
	}
}
