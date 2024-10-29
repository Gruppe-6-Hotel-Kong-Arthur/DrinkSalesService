from flask import Flask, jsonify, request, Blueprint
from repositories.drink_sales_repository import (
    db_get_all_drink_sales,
    db_update_units_sold
    )



# Blueprint for drink sales routes
drink_sales_routes = Blueprint('drink__sales_routes', __name__)


# GET all drink sales
@drink_sales_routes.route('', methods=['GET'])
def get_all_drink_sales():
    try:
        drink_sales = db_get_all_drink_sales()
        return jsonify(drink_sales), 200 if drink_sales else 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
# PATCH update units sold for a drink
@drink_sales_routes.route('/<int:drink_id>', methods=['PATCH'])
def update_units_sold(drink_id):
    try:
        data = request.get_json()
        amount_of_units_sold = data.get("amount_of_units_sold")

        # Validate input
        if amount_of_units_sold is None or not isinstance(amount_of_units_sold, int):
            return jsonify({"error": "Invalid or missing 'amount_of_units_sold'"}), 400

        db_update_units_sold(drink_id, amount_of_units_sold)
        return jsonify({"message": "Units sold updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
