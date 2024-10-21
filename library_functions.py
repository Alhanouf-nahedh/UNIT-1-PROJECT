import json

BOOK_FILE = 'data/books.json'

def load_books():
    with open(BOOK_FILE, 'r') as f:
        return json.load(f)

def save_books(books):
    with open(BOOK_FILE, 'w') as f:
        json.dump(books, f, indent=4)

def list_books():
    books = load_books()
    for book in books:
        print(f"ID: {book['id']}")
        print(f"Title: {book['title']}")
        print(f"Author: {book['author']}")
        print(f"Year: {book['year']}")
        print()

def book_details(book_id):
    books = load_books()
    book_id = int(book_id)
    for book in books:
        if book['id'] == book_id:
            print(f"Title: {book['title']}")
            print(f"Author: {book['author']} ({book['year']})")
            print(f"Description: {book['description']}")
            print(f"Likes: {book['likes']}")
            print(f"Comments: {book['comments']}")
            print(f"Ratings: {book['ratings']}")
            if book['ratings']:
                average_rating = sum(book['ratings']) / len(book['ratings'])
                print(f"Average Rating: {average_rating:.1f}")
            else:
                print("Average Rating: No ratings yet.")
            break
    else:
        print("Book not found!")


def like_book(book_id):
    book_id = int(book_id)
    books = load_books()
    for book in books:
        if book['id'] == book_id:
            book['likes'] += 1
            save_books(books)
            print(f"You liked '{book['title']}'. Total Likes: {book['likes']}")
            break
    else:
        print("Book not found!")

def comment_book(book_id, type_comment):
    book_id = int(book_id)
    books = load_books()
    for book in books:
        if book['id'] == book_id:
            book['comments'].append(type_comment)
            save_books(books)
            print(f"Comment added to '{book['title']}'.")
            break
    else:
        print("Book not found!")
   
def rate_book(book_id, rating):
    book_id = int(book_id)
    books = load_books()
    for book in books:
        if book['id'] == book_id:
            book['ratings'].append(rating)
            save_books(books)
            print(f"Rating of {rating} added to '{book['title']}'.")
            break
    else:
        print("Book not found!")
        
def add_book():
    books = load_books()
    if books:
        new_id = max(book['id'] for book in books) + 1  # add 1 to the max id
    else:
        new_id = 1

    title = input("Enter book title: ")
    author = input("Enter author name: ")
    year = int(input("Enter year: "))
    description = input("Enter description: ")

    new_book = {
        "id": new_id,
        "title": title,
        "author": author,
        "year": year,
        "description": description,
        "likes": 0,
        "comments": [],
        
    }

    books.append(new_book)
    save_books(books)
    print(f"Book '{title}' added successfully!")
    
def delete_book(book_id):
    book_id = int(book_id)
    books = load_books()
    for book in books:
        if book['id'] == book_id:
            books.remove(book)
            save_books(books)
            print(f"Book '{book['title']}' deleted successfully!")
            break
    else:
        print("Book not found!")