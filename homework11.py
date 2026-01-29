import sqlite3

# =========================
# TASK 1 — roster.db


conn1 = sqlite3.connect("roster.db")
cur1 = conn1.cursor()

# Create table

cur1.execute("""
CREATE TABLE IF NOT EXISTS Roster (
    Name TEXT,
    Species TEXT,
    Age INTEGER
)
""")

# Insert data

cur1.executemany("""
INSERT INTO Roster (Name, Species, Age)
VALUES (?, ?, ?)
""", [
    ("Benjamin Sisko", "Human", 40),
    ("Jadzia Dax", "Trill", 300),
    ("Kira Nerys", "Bajoran", 29)
])

conn1.commit()

# Update name

cur1.execute("""
UPDATE Roster
SET Name = "Ezri Dax"
WHERE Name = "Jadzia Dax"
""")

conn1.commit()

# Query Bajoran species

print("\n--- Bajoran Characters ---")
for row in cur1.execute("""
SELECT Name, Age FROM Roster WHERE Species = "Bajoran"
"""):
    print(row)

# Delete age > 100

cur1.execute("""
DELETE FROM Roster WHERE Age > 100
""")

conn1.commit()

# Add Rank column

cur1.execute("""
ALTER TABLE Roster ADD COLUMN Rank TEXT
""")

# Update ranks

cur1.execute("UPDATE Roster SET Rank='Captain' WHERE Name='Benjamin Sisko'")
cur1.execute("UPDATE Roster SET Rank='Lieutenant' WHERE Name='Ezri Dax'")
cur1.execute("UPDATE Roster SET Rank='Major' WHERE Name='Kira Nerys'")

conn1.commit()

# Advanced query — sort by age desc

print("\n--- Roster Sorted by Age (DESC) ---")
for row in cur1.execute("""
SELECT * FROM Roster ORDER BY Age DESC
"""):
    print(row)

conn1.close()


# =========================
# TASK 2 — library.db


conn2 = sqlite3.connect("library.db")
cur2 = conn2.cursor()

# Create table

cur2.execute("""
CREATE TABLE IF NOT EXISTS Books (
    Title TEXT,
    Author TEXT,
    Year_Published INTEGER,
    Genre TEXT
)
""")

# Insert data

cur2.executemany("""
INSERT INTO Books (Title, Author, Year_Published, Genre)
VALUES (?, ?, ?, ?)
""", [
    ("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction"),
    ("1984", "George Orwell", 1949, "Dystopian"),
    ("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Classic")
])

conn2.commit()

# Update year of 1984

cur2.execute("""
UPDATE Books
SET Year_Published = 1950
WHERE Title = "1984"
""")

conn2.commit()

# Query dystopian books

print("\n--- Dystopian Books ---")
for row in cur2.execute("""
SELECT Title, Author FROM Books WHERE Genre = "Dystopian"
"""):
    print(row)

# Delete books before 1950

cur2.execute("""
DELETE FROM Books WHERE Year_Published < 1950
""")

conn2.commit()

# Add Rating column

cur2.execute("""
ALTER TABLE Books ADD COLUMN Rating REAL
""")

# Update ratings

cur2.execute("UPDATE Books SET Rating=4.8 WHERE Title='To Kill a Mockingbird'")
cur2.execute("UPDATE Books SET Rating=4.7 WHERE Title='1984'")
cur2.execute("UPDATE Books SET Rating=4.5 WHERE Title='The Great Gatsby'")

conn2.commit()

# Advanced query — sort by year asc

print("\n--- Books Sorted by Year (ASC) ---")
for row in cur2.execute("""
SELECT * FROM Books ORDER BY Year_Published ASC
"""):
    print(row)

conn2.close()

print("\n✅ All tasks completed successfully!")
