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
