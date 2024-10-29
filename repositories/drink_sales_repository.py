from database.connection import create_connection

# Retrieve all drink sales data
def db_get_all_drink_sales():
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM drink_sales")
    drink_sales = cursor.fetchall()

    connection.close()

    return [dict(row) for row in drink_sales]

# Update amont of units sold for a drink
def db_update_units_sold(drink_id, amount_of_units_sold):
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE drink_sales
        SET units_sold = units_sold + ?
        WHERE drink_id = ?
    """, (amount_of_units_sold, drink_id))

    connection.commit()
    connection.close()

