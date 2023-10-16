import java.util.Random;
import java.util.Scanner;

public class Main {
	public static int arrayLength(String[] arr) {
		int count = 0;
		for (String element : arr) {
			count++;
		}
		return count;
	}
	public static void main(String args[]) {
		Scanner scan = new Scanner(System.in);
		BookList bookList = new BookList();
		String[] bookInfo = null;
		System.out.println("Welcome to the book program!\n");

		while (true) {
			System.out.print("Would you like to create a book object? (yes/no): ");
			String userChoice = scan.next().toLowerCase();
			while (!userChoice.equals("yes") && !userChoice.equals("no")) {
				System.out.print(String.format("\nI'm sorry but %s isn't a valid answer. Please enter either yes or no: ", userChoice) );
				userChoice = scan.next().toLowerCase();
				System.out.print("\n");
			}
			if (userChoice.equals("no")) {
				break;
			} else if (userChoice.equals("yes")) {
				scan.nextLine();

				String author;
				String title;
				String isbn;
				do {
					System.out.print("\nPlease enter the author, title, and the isbn of the book separated by /: ");
					bookInfo = scan.nextLine().split("/");
					while (arrayLength(bookInfo) != 3) {
						System.out.print("\nPlease enter the author, title, and the isbn of the book separated by /: ");
						bookInfo = scan.nextLine().split("/");
					}
					while (bookInfo[0].length() < 3) {
						System.out.print("\nPlease enter an authors name of at least 3 characters or more: ");
						bookInfo[0] = scan.nextLine();
					}


				} while (bookInfo == null);
				author = bookInfo[0].trim();
				title = bookInfo[1].trim();
				isbn = bookInfo[2].trim();
				System.out.println("\nGot it!");
				String bookLocation = "";

				System.out.print("\nNow, tell me if it is a bookstore book or a library book (enter BB for bookstore book or LB for library book): ");
				bookLocation = scan.next().toLowerCase();
				while (!bookLocation.equals("bb") && !bookLocation.equals("lb")) {
					System.out.print("\nOops! That's not a valid entry. Please try again: ");
					bookLocation = scan.next().toLowerCase();
				}
				System.out.println("\nGot it!");


				if (bookLocation.equals("bb")) {
					double bookPrice = 0;
					boolean validPrice = false;
					while (!validPrice) {
						System.out.print(String.format("\nPlease enter the list price of %s by %s: ", title.toUpperCase(), author.toUpperCase()));
						if (scan.hasNextDouble()) {
							bookPrice = scan.nextDouble();
							validPrice = true;
						} else {
							System.out.print("\nInvalid input. Please enter a valid price such as 15.99");
							scan.next();
						}
					}

					System.out.print("\nIs it on sale? (yes/no):");
					String onSale = scan.next().toLowerCase();
					while (!onSale.equals("yes") && !onSale.equals("no")) {
						System.out.print(String.format("\nI'm sorry but %s isn't a valid answer. Please enter either yes or no: ", onSale) );
						onSale = scan.next().toLowerCase();
						System.out.print("\n");
					}
					if (onSale.equals("yes")) {
						System.out.print("\nDeduction percentage: ");
						String reductionPercent = "0";
						reductionPercent = scan.next();
						reductionPercent = reductionPercent.replaceAll("%", "").trim();
						int reductionPercentage = Integer.parseInt(reductionPercent);
						while (reductionPercentage < 0 || reductionPercentage > 100) {
							System.out.print("\nPlease enter a Deduction Percentage below 100 and above -1: ");
							reductionPercent = scan.nextLine();
							reductionPercent = reductionPercent.replaceAll("%", "").trim();
							reductionPercentage = Integer.parseInt(reductionPercent);

						}
						bookList.addBook(new BookstoreBook(author, title, isbn, bookPrice, reductionPercentage, true));
						double reducedPrice = bookPrice - (bookPrice * ((double)reductionPercentage/100));
						System.out.println("\nGot it!");
						System.out.println("\n\n\nHere is your bookstore book information");
						System.out.println(String.format("\n[%s-%s by %s, $%.2f listed for $%.2f]\n\n", isbn, title.toUpperCase(), author.toUpperCase(), bookPrice, reducedPrice) );

					} else {
						bookList.addBook(new BookstoreBook(author, title, isbn, bookPrice, 0, false));
					}


				} else if (bookLocation.equals("lb")) {
					LibraryBook lib = new LibraryBook(author, title, isbn);
					bookList.addBook(lib);
					System.out.println("\n\n\nHere is your library book information\n");
					System.out.println(String.format("[%s-%s by %s-%s]\n\n", isbn, title.toUpperCase(), author.toUpperCase(), lib.getCallNum()));
				}
			}
		}
		System.out.println("\nSure!\n\n");
		System.out.println("\nHere are all your books...\n");
		bookList.listBooks();
		System.out.println("Take care now!");
		scan.close();
	}


}
//_______________
abstract class Book {
	private String author;
	private String title;
	private String isbn;

	public String getAuthor() {
		return author;
	}

	public void setAuthor(String author) {
		this.author = author;
	}

	public String getTitle() {
		return title;
	}

	public void setTitle(String title) {
		this.title = title;
	}

	public String getIsbn() {
		return isbn;
	}

	public void setIsbn(String isbn) {
		this.isbn = isbn;
	}

	public Book(String author, String title, String isbn) {
		this.author = author;
		this.title = title;
		this.isbn = isbn;
	}
	public Book(String title, String isbn) {
		author = "UNKNOWN AUTHOR";
		this.title = title;
		this.isbn = isbn;
	}
	public Book(String isbn) {
		author = "UNKNOWN AUTHOR";
		title = "UNTITLED";
		this.isbn = isbn;
	}

	public abstract String toString();

}
//___________________________
class BookstoreBook extends Book {

	private double bookPrice;
	private boolean onSale;
	private int reductionPercent;

	public double getBookPrice() {
		return bookPrice;
	}
	public void setBookPrice(double bookPrice) {
		this.bookPrice = bookPrice;
	}
	public boolean isOnSale() {
		return onSale;
	}
	public void setOnSale(boolean onSale) {
		this.onSale = onSale;
	}
	public int getReductionPercent() {
		return reductionPercent;
	}
	public void setReductionPercent(int reductionPercent) {
		this.reductionPercent = reductionPercent;
	}

	public BookstoreBook(String author, String title, String isbn, double bookPrice, int reductionPercent, boolean onSale) {
		super(author, title, isbn);
		this.bookPrice = bookPrice;
		this.reductionPercent = reductionPercent;
		this.onSale = onSale;
	}
	public BookstoreBook(String title, String isbn, double bookPrice, int reductionPercent, boolean onSale) {
		super(title, isbn);
		this.bookPrice = bookPrice;
		this.reductionPercent = reductionPercent;
		this.onSale = onSale;
	}
	public BookstoreBook(String isbn, double bookPrice, int reductionPercent, boolean onSale) {
		super(isbn);
		this.bookPrice = bookPrice;
		this.reductionPercent = reductionPercent;
		this.onSale = onSale;
	}
	@Override
	public String toString() {//double reducedPrice = bookPrice - (bookPrice * ((double)reductionPercentage/100));
		return String.format("[%s-%s by %s, $%.2f listed for $%.2f]", getIsbn(), getTitle().toUpperCase(), getAuthor().toUpperCase(), bookPrice, (bookPrice - (bookPrice * ((double)reductionPercent / 100)) ) );
	}


}
//___________________________
class LibraryBook extends Book {
	private String callNum;

	public String getCallNum() {
		return callNum;
	}

	public void setCallNum(String callNum) {
		this.callNum = callNum;
	}

	public LibraryBook(String author, String title, String isbn) {
		super(author, title, isbn);
		this.callNum = callNumberGen(author, isbn);
	}
	public LibraryBook(String title, String isbn) {
		super(title, isbn);
		this.callNum = callNumberGen("UNKOWN AUTHOR", isbn);
	}
	public LibraryBook(String isbn) {
		super(isbn);
		this.callNum = callNumberGen("UNKOWN AUTHOR", isbn);
	}

	private String callNumberGen(String author, String isbn) {
		Random rand = new Random();
		int floorNum = rand.nextInt(99)+1;
		String authorCode = author.substring(0, 3).toUpperCase();
		char isbnLastChar = isbn.charAt(isbn.length() - 1);
		return String.format("%02d.%s.%c", floorNum, authorCode, isbnLastChar);
	}

	@Override
	public String toString() {
		return String.format("[%s-%s by %s-%s]", getIsbn(), getTitle().toUpperCase(), getAuthor().toUpperCase(), callNum );
	}
	// fields and specific code to the LibraryBook class goes here
}
//___________________________
class BookList {
	private Book[] list;
	private int books;

	public BookList() {
		list = new Book[100];
		books = 0;
	}

	public void addBook(Book book) {
		if (books < 100) {
			list[books] = book;
			books++;
		}
	}

	public void listBooks() {
		int libraryCount = 0;
		int bookstoreCount = 0;

		for (int index = 0; index < books; index++) {
			if (list[index] instanceof LibraryBook) {
				libraryCount++;
			} else if (list[index] instanceof BookstoreBook) {
				bookstoreCount++;
			}
		}


		System.out.println(String.format("Library Books (%d)", libraryCount));
		for (Book book : list) {
			if (book instanceof LibraryBook) {
				System.out.println("\n\t"+book);
			}
		}
		System.out.println("\n_ _ _ _\n");
		System.out.println(String.format("Bookstore Books (%d)", bookstoreCount));
		for (Book book : list) {
			if (book instanceof BookstoreBook) {
				System.out.println("\n\t"+book);
			}
		}
		System.out.println("\n_ _ _ _\n");
	}


}
