import sqlite3
from lib.db.connection import get_connection

def seed():
    conn = get_connection()
    cursor = conn.cursor()

    # Insert authors
    authors = [("Jane Doe",), ("John Smith",), ("Alice Johnson",)]
    cursor.executemany("INSERT INTO authors (name) VALUES (?)", authors)

    # Insert magazines
    magazines = [("Tech Today", "Technology"), ("Health Weekly", "Health"), ("Science Monthly", "Science")]
    cursor.executemany("INSERT INTO magazines (name, category) VALUES (?, ?)", magazines)

    # Insert articles
    # We assume author ids 1,2,3 and magazine ids 1,2,3 for simplicity
    articles = [
        ("AI and Future", 1, 1),
        ("Healthy Living Tips", 2, 2),
        ("Quantum Mechanics Simplified", 3, 3),
        ("Tech Trends 2025", 1, 1),
        ("Nutrition and Wellness", 2, 2)
    ]
    cursor.executemany("INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)", articles)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    seed()
