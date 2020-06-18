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
			database.add_books()
		elif user_input == "l":
			reading_list = database.list_all_books()
			if reading_list:
				database.list_books(reading_list)
			else:
				print("List is empty")
		elif user_input == "r":
			database.mark_book_as_read()
		elif user_input == "d":
			database.delete_books()
		else:
			print("Input is not valid, please enter again")

		user_input = input(USER_CHOICE).strip().lower()


menu()
