import json
import os
from datetime import datetime

DATA_FILE = "books.json"

def load_books():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def save_books(books):
    with open(DATA_FILE, "w") as f:
        json.dump(books, f, indent=4)

def add_book(books):
    title = input("Enter book title: ").strip()
    if any(b["title"].lower() == title.lower() for b in books):
        print("Book with this title already exists!")
        return
    
    author = input("Enter author: ").strip()
    while True:
        try:
            total_pages = int(input("Enter total pages: "))
            if total_pages <= 0:
                print("Pages must be positive.")
                continue
            break
        except ValueError:
            print("Enter a valid number.")
    
    start_date = datetime.now().strftime("%Y-%m-%d")
    print(f"Start date set to today: {start_date}")
    
    book = {
        "title": title,
        "author": author,
        "total_pages": total_pages,
        "pages_read": 0,
        "start_date": start_date,
        "finish_date": None,
        "rating": None,
        "status": "Reading"
    }
    books.append(book)
    save_books(books)
    print("Book added successfully!")

def update_progress(books):
    title = input("Enter book title to update: ").strip()
    book = next((b for b in books if b["title"].lower() == title.lower()), None)
    if not book:
        print("Book not found.")
        return
    if book["status"] == "Finished":
        print("Book already finished.")
        return
    
    while True:
        try:
            pages = int(input("Enter pages read today: "))
            if pages < 0:
                print("Cannot be negative.")
                continue
            break
        except ValueError:
            print("Enter a valid number.")
    
    book["pages_read"] += pages
    if book["pages_read"] > book["total_pages"]:
        book["pages_read"] = book["total_pages"]
    
    save_books(books)
    print(f"Progress updated. {book['pages_read']}/{book['total_pages']} pages ({book['pages_read']/book['total_pages']*100:.1f}%)")

def finish_book(books):
    title = input("Enter book title to finish: ").strip()
    book = next((b for b in books if b["title"].lower() == title.lower()), None)
    if not book:
        print("Book not found.")
        return
    if book["status"] == "Finished":
        print("Already finished.")
        return
    
    while True:
        try:
            rating = int(input("Enter rating (1-5): "))
            if 1 <= rating <= 5:
                break
            print("Rating must be 1 to 5.")
        except ValueError:
            print("Enter a number 1-5.")
    
    book["finish_date"] = datetime.now().strftime("%Y-%m-%d")
    book["rating"] = rating
    book["status"] = "Finished"
    book["pages_read"] = book["total_pages"]  # ensure full
    save_books(books)
    print("Book marked as finished!")

def list_books(books):
    if not books:
        print("No books added yet.")
        return
    
    print("\nYour Books:")
    print("-" * 60)
    for b in books:
        progress = b["pages_read"] / b["total_pages"] * 100 if b["total_pages"] > 0 else 0
        rating_str = str(b["rating"]) if b["rating"] else "-"
        print(f"Title     : {b['title']}")
        print(f"Author    : {b['author']}")
        print(f"Progress  : {b['pages_read']}/{b['total_pages']} ({progress:.1f}%)")
        print(f"Status    : {b['status']}")
        print(f"Rating    : {rating_str}")
        print(f"Started   : {b['start_date']}")
        print(f"Finished  : {b['finish_date'] or '-'}")
        print("-" * 60)

def show_stats(books):
    if not books:
        print("No books yet.")
        return
    
    finished = [b for b in books if b["status"] == "Finished"]
    count_finished = len(finished)
    total_pages_read = sum(b["pages_read"] for b in books)
    avg_rating = sum(b["rating"] for b in finished) / count_finished if count_finished > 0 else 0
    
    print("\nReading Statistics:")
    print(f"Books finished   : {count_finished}")
    print(f"Total pages read : {total_pages_read}")
    print(f"Average rating   : {avg_rating:.1f}" if count_finished > 0 else "No finished books yet")

def main():
    books = load_books()
    
    while True:
        print("\nBook Reading Tracker")
        print("1. Add new book")
        print("2. Update reading progress")
        print("3. Finish a book & rate")
        print("4. List all books")
        print("5. Show statistics")
        print("6. Exit")
        
        choice = input("Enter choice (1-6): ").strip()
        
        if choice == "1":
            add_book(books)
        elif choice == "2":
            update_progress(books)
        elif choice == "3":
            finish_book(books)
        elif choice == "4":
            list_books(books)
        elif choice == "5":
            show_stats(books)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
