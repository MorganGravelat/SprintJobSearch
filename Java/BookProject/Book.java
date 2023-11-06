public class Book {
    private String name;
    private String description;
    private String publisher;
    private String text;

    public Book(String name, String description, String publisher, String text) {
        this.name = name;
        this.description = description;
        this.publisher = publisher;
        this.text = text;
    }

    // Getters and setters for the book properties
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public String getPublisher() {
        return publisher;
    }

    public void setPublisher(String publisher) {
        this.publisher = publisher;
    }

    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }

    @Override
    public String toString() {
        return "Name: " + name + "\nDescription: " + description + "\nPublisher: " + publisher + "\nText: " + text;
    }
}
