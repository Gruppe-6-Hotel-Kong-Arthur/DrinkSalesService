import sqlite3

# Create or connect to SQLite database
def create_connection():
    connection = sqlite3.connect('database/drinks_sales.db')
    connection.row_factory = sqlite3.Row 
    return connection
