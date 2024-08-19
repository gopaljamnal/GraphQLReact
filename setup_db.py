import sqlite3

# Connect to SQLite database (creates the file if it doesn't exist)
conn = sqlite3.connect('users.db')

# Create a cursor object
cursor = conn.cursor()

# Create the users table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL
)
''')

# Insert some initial data into the users table
cursor.execute('''
INSERT INTO users (name, email)
VALUES
    ('John Doe', 'john@example.com'),
    ('Jane Smith', 'jane@example.com')
''')

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database setup complete.")
