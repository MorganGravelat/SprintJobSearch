import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.util.ArrayList;
import java.util.List;

public class BookReader {
    public List<Book> readBooks(String filename) {
        List<Book> books = new ArrayList<>();
        searchFiles(new File("."), filename, books);
        return books;
    }

    private void searchFiles(File directory, String filename, List<Book> books) {
        File[] files = directory.listFiles();
        if (files != null) {
            for (File file : files) {
                if (file.isDirectory()) {
                    searchFiles(file, filename, books);
                } else if (file.getName().equals(filename)) {
                    try {
                        String content = new String(Files.readAllBytes(file.toPath()));
                        Book book = parseBook(content);
                        books.add(book);
                    } catch (IOException e) {
                        e.printStackTrace();
                    }
                }
            }
        }
    }

    private Book parseBook(String content) {
        String[] lines = content.split("\n");
        String name = "";
        String description = "";
        String publisher = "";
        String text = "";

        for (String line : lines) {
            if (line.startsWith("Name:")) {
                name = line.substring("Name:".length()).trim();
            } else if (line.startsWith("Description:")) {
                description = line.substring("Description:".length()).trim();
            } else if (line.startsWith("Publisher:")) {
                publisher = line.substring("Publisher:".length()).trim();
            } else if (line.startsWith("Text:")) {
                text = line.substring("Text:".length()).trim();
            }
        }

        return new Book(name, description, publisher, text);
    }
}
