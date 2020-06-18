def add_books():
    name = input("Enter book name :").lower().strip()
    author = input("Enter author name :").lower().strip()

    book = f'{name},{author},Not read\n'
    with open('books.csv','a') as reading_list:
        reading_list.write(book)

def list_all_books():
    books = []
    with open('books.csv', 'r')as reading_list:
        for book in reading_list:
            title, author, read_status = book.strip().split(",")

            books.append({
                "title": title,
                 "author": author,
                "read": read_status

            })
    return books

def list_books(books):
    for book in books:
        print(f"{book['title']}, by {book['author']} - {book['read']}")

def find_books():
    reading_list = list_all_books()
    matching_books = []
    search_term = input("Enter the title name to delete the book : ").strip().lower()
    for book in reading_list:
        if search_term in book['title'].lower():
            matching_books.append(book)
    return matching_books

def delete_books():
    books = list_all_books()
    matching_books = find_books()
    if matching_books :
        books.remove(matching_books[0])
        with open("books.csv", "w") as reading_list:
            for book in books:
                reading_list.write(f"{book['title']},{book['author']},{book['read']}\n")
    else:
        print("Sorry, we didn't find any books matching that title.")


def mark_book_as_read():
    books = list_all_books()
    matching_books = find_books()

    if matching_books :
        index = books.index(matching_books[0])
        books[index]['read'] = 'Read'

        with open("books.csv" ,"w") as reading_list:
            for book in books :
                reading_list.write(f"{book['title']},{book['author']},{book['read']}\n")



    else:
        print("Not matching book found")
