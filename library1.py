import csv

BOOK_FILE = "books.csv"
MEMBER_FILE = "members.csv"
ISSUE_FILE = "issues.csv"

def load_csv(filename):
    try:
        with open(filename, "r", newline="") as f:
            return list(csv.DictReader(f))
    except FileNotFoundError:
        return []

def save_csv(filename, data, fieldnames):
    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def add_book():
    books = load_csv(BOOK_FILE)
    bid = input("Enter Book ID: ")
    title = input("Enter Title: ")
    author = input("Enter Author: ")
    available = "Yes"
    books.append({"BookID": bid, "Title": title, "Author": author, "Available": available})
    save_csv(BOOK_FILE, books, ["BookID", "Title", "Author", "Available"])
    print("Book added successfully!\n")

def display_books():
    books = load_csv(BOOK_FILE)
    print("\n--- Book List ---")
    for b in books:
        print(f"{b['BookID']} | {b['Title']} | {b['Author']} | Available: {b['Available']}")
    print()

def delete_book():
    books = load_csv(BOOK_FILE)
    bid = input("Enter Book ID to delete: ")
    books = [b for b in books if b['BookID'] != bid]
    save_csv(BOOK_FILE, books, ["BookID", "Title", "Author", "Available"])
    print("Book deleted (if existed).\n")
