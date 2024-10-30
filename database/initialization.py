import pandas as pd
import os
from database.connection import create_connection

def init_db():
    # Specify the Excel file and SQLite database file path
    excel_file = "xlxs/drinks_menu_with_sales.xlsx"
    sqlite_db = os.path.join(os.getcwd(), "drink_sales.db")

    if os.path.exists(sqlite_db):
        os.remove(sqlite_db)

    # Read Excel file (assuming 'Sheet1' has the data)
    data = pd.read_excel(excel_file, sheet_name="Sheet1")

    # Connect to SQLite database
    connection = create_connection()
    cursor = connection.cursor()

    # Create the drink_sales table
    cursor.execute("""CREATE TABLE IF NOT EXISTS drink_sales (
            drink_id INTEGER PRIMARY KEY,
            units_sold INTEGER NOT NULL
        )
    """)
    # Insert data into the drink_sales table
    for i, row in data.iterrows():
        units_sold = row['Units Sold'] 

        cursor.execute("""
            INSERT INTO drink_sales (units_sold)
            VALUES (?)
        """, (units_sold,))

    connection.commit()
    connection.close()
        

    
