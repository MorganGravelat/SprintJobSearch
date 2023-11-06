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
