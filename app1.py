from utils import database
USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit
Your choice: """

def menu():
	user_input = input(USER_CHOICE).strip().lower()
	while user_input != "q":
		if user_input == "a":
			prompt_add_books()
		elif user_input == "l":
			list_books()
		elif user_input == "r":
			promt_read_book()
		elif user_input == "d":
			prompt_delete_book()
		else:
			print("Input is not valid, please enter again")

		user_input = input(USER_CHOICE).strip().lower()


def prompt_add_books():
	name = input("Enter Book name: ")
	author = input("Enter Author name: ")
	year = input("Enter published year")

	books = database.add_books(name,author,year)

def list_books():
	books = database.list_all_books()
	if not books:
		print("The database is empty")
		return
	for book in books:
			read = "YES" if book['read'] == "1" else "NO"
			print(f"{book['name']}, by {book['author']} -{book['year']} -- read:{read}")



def promt_read_book():
	name = input("Enter book name you have just finished: ").strip().lower()
	books = database.read_all_books(name)


def prompt_delete_book():
	name = input("Enter book name you want to delete: ")
	books = database.delete_books(name)

menu()
