import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the filename to search for: ");
        String filename = scanner.nextLine();

        BookReader bookReader = new BookReader();
        List<Book> books = bookReader.readBooks(filename);

        if (books.isEmpty()) {
            System.out.println("No books found with that filename.");
        } else {
            System.out.println("Found the following books:");
            for (Book book : books) {
                System.out.println(book);
            }
        }
    }
}
