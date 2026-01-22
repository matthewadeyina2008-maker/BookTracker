# BookReadingTracker

A simple console-based personal book reading tracker written in Python.

Track the books you're reading, update your progress, mark books as finished with ratings, and view basic statistics — all stored locally in a JSON file.

## Features

- Add new books with title, author, total pages, and automatic start date
- Update reading progress (add pages read)
- Mark books as finished and give them a rating (1–5)
- List all books with current status, progress percentage, and details
- View reading statistics:
  - Number of books finished
  - Total pages read
  - Average rating of finished books
- Persistent storage (data saved in `books.json`)

## Requirements

- Python 3.6+
- No external libraries required (uses only standard library: `json`, `os`, `datetime`)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/YOUR_USERNAME/BookReadingTracker.git
   cd BookReadingTracker

python -m venv venv
# Activate it:
# Linux / macOS
source venv/bin/activate
# Windows
venv\Scripts\activate


*Project Name:** BookReadingTracker

**Main features:**
- Add a new book (title, author, total pages, start date)
- Update reading progress (pages read)
- Mark book as finished + give rating (1–5)
- List all books with status & progress
- View reading statistics (books finished, total pages read, average rating)
- Data saved to/loaded from JSON file

Technology: Python 3 (console app, no external libs beyond standard library)

Now I'll walk through the **full SDLC** (using classic Waterfall model, common for assignments), then give the complete code that matches all names exactly.

### 1. Planning / Feasibility Study
- Objective: Build console app to help users track book reading habits.
- Scope: Console only, local JSON storage, basic CRUD + stats.
- Resources: Python 3, standard lib (json, datetime, os).
- Time: 4–8 hours for student.
- Feasibility: High — simple logic, no UI/API/database server needed.

### 2. Requirements Gathering & Analysis
**Functional Requirements:**
- User can add book → title (str), author (str), total_pages (int), start_date (YYYY-MM-DD str)
- User can update progress → enter book title + pages read today
- User can finish book → enter title + rating (1–5)
- User can view all books (show title, author, progress %, status: Reading/Finished, rating if done)
- User can view stats: finished count, total pages read, avg rating
- Data persists between runs (JSON file)

**Non-Functional:**
- Simple console menu
- Input validation (basic)
- File: books.json in same folder

### 3. System Design
**High-Level Design:**
- Single Python file: book_tracker.py
- Data structure: list of dicts
  ```python
  {
      "title": str,
      "author": str,
      "total_pages": int,
      "pages_read": int = 0,
      "start_date": str,
      "finish_date": str or None,
      "rating": int or None,
      "status": "Reading" or "Finished"
  }
  ```
- Main menu loop
- Functions: load_books(), save_books(), add_book(), update_progress(), finish_book(), list_books(), show_stats()

**File:** books.json (list of above dicts)

**Low-Level:** Functions use exact names as shown.

### 4. Implementation (Coding)
### 5. Testing
- Unit test mentally: add → check file, update → progress increases, finish → status & rating set, list → shows correctly, stats → calculates right.
- Edge cases: zero pages, duplicate titles, invalid input → handled basically.
- Run multiple times → data persists.

### 6. Deployment
- Just run: `python book_tracker.py`
- For GitHub: create repo → add file → commit → push.

### 7. Maintenance
- Future: add delete book, search, sort by rating/date, export CSV.

**GitHub Steps (do this yourself):**
1. Go to github.com → New repository
2. Name: BookReadingTracker (or Book-Reading-Tracker)
3. Public / Private (your choice)
4. Create repo
5. Locally: `git init`, `git add book_tracker.py`, `git commit -m "Initial commit - Book Reading Tracker completed"`, `git remote add origin https://github.com/yourusername/BookReadingTracker.git`, `git push -u origin main`
6.
