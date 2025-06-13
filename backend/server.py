from flask import Flask, request, jsonify
import products_dao
from sql_connection import  get_sql_connection

app = Flask(__name__)

@app.route('/get_products', methods=['GET'])
def get_products():
    products_dao.get_all_products(connection)


if __name__ == '__main__':
    print("Starting server...")
    app.run(port=5000)
