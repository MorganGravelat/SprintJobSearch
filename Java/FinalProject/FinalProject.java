public class Student {
    private String fullName;
    private String id;
    private double gpa;
    private int numberOfCreditHours;

    public Student(String fullName, String id, double gpa, int numberOfCreditHours) {
        this.fullName = fullName;
        this.id = id;
        this.gpa = gpa;
        this.numberOfCreditHours = numberOfCreditHours;
    }

    // Getters and Setters
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

    public double getGpa() {
        return gpa;
    }

    public void setGpa(double gpa) {
        this.gpa = gpa;
    }

    public int getNumberOfCreditHours() {
        return numberOfCreditHours;
    }

    public void setNumberOfCreditHours(int numberOfCreditHours) {
        this.numberOfCreditHours = numberOfCreditHours;
    }
}

public class Faculty {
    private String fullName;
    private String id;
    private String department; // mathematics, engineering, or english
    private String rank; // professor or adjunct

    public Faculty(String fullName, String id, String department, String rank) {
        this.fullName = fullName;
        this.id = id;
        this.department = department;
        this.rank = rank;
    }

    // Getters and Setters
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

    public String getDepartment() {
        return department;
    }

    public void setDepartment(String department) {
        this.department = department;
    }

    public String getRank() {
        return rank;
    }

    public void setRank(String rank) {
        this.rank = rank;
    }
}

public class Staff {
    private String fullName;
    private String id;
    private String department; // mathematics, engineering, or english
    private String status; // part time or full time

    public Staff(String fullName, String id, String department, String status) {
        this.fullName = fullName;
        this.id = id;
        this.department = department;
        this.status = status;
    }

    // Getters and Setters
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

    public String getDepartment() {
        return department;
    }

    public void setDepartment(String department) {
        this.department = department;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
}
