book_list = "books.csv"


def add_books(name, author, year):
    with open( book_list , "a") as file:
        file.write(f'{name},{author},{year},0\n')



def list_all_books():
    books = []

    with open("books.csv", "r") as reading_list:
        for book in reading_list:
            title, author, year, read_status = book.strip().split(",")

            books.append({
                "name": title,
                "author": author,
                "year": year,
                "read": read_status
            })
    return books


def read_all_books(name):
    books = list_all_books()
    for book in books:
        if book['name'] == name :
            book['read'] = '1'
    _save_all_books(books)

def _save_all_books(books):
    with open (book_list, "w")as file:
        for book in books:
            file.write(f"{book['name']},{book['author']},{book['year']},{book['read']}\n")



def delete_books(name):
    books = list_all_books()
    books = [book for book in books if book['name'] != name]
    _save_all_books(books)
