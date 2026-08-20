from flask import Flask, request, jsonify
from sql_connection import get_sql_connection
import mysql.connector
import json

import products_dao
import orders_dao
import uom_dao

import os

ui_folder_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'ui'))
app = Flask(__name__, static_folder=ui_folder_path, static_url_path='')

@app.route('/')
def index():
    return app.send_static_file('index.html')

connection = get_sql_connection()

@app.route('/getUOM', methods=['GET'])
def get_uom():
    response = uom_dao.get_uoms(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/getProducts', methods=['GET'])
def get_products():
    response = products_dao.get_all_products(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/insertProduct', methods=['POST'])
def insert_product():
    request_payload = json.loads(request.form['data'])
    product_id = products_dao.insert_new_product(connection, request_payload)
    response = jsonify({
        'product_id': product_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/getAllOrders', methods=['GET'])
def get_all_orders():
    response = orders_dao.get_all_orders(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/insertOrder', methods=['POST'])
def insert_order():
    request_payload = json.loads(request.form['data'])
    order_id = orders_dao.insert_order(connection, request_payload)
    response = jsonify({
        'order_id': order_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/deleteProduct', methods=['POST'])
def delete_product():
    try:
        return_id = products_dao.delete_product(connection, request.form['product_id'])
        response = jsonify({
            'product_id': return_id
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as e:
        response = jsonify({
            'error': 'Cannot delete product because it is associated with existing orders.'
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response, 400

if __name__ == "__main__":
    print("Starting Python Flask Server For Grocery Store Management System")
    app.run(port=5000)

