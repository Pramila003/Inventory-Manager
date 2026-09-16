from models import Product, Order, Supplier
from datetime import datetime
import json

def load_products():
    try:
        with open (r"C:\Users\Admin\Desktop\pythoncc\inventory-manager\data\products.json","r") as file:
            product_data = json.load(file)

    except FileNotFoundError:
        return []

    products =[] 

    for data in product_data:
        product = Product(data["id"],data["name"],data["category"],data["price"],data["quantity"],data["supplier_id"],data["reorder_level"])

        products.append(product)

    return products

def save_products(products):
    product_data = []

    for product in products:
        product_dict = product.to_dict()
        product_data.append(product_dict)

    try:
        with open(r"data\products.json","w") as file:
            json.dump(product_data,file, intent=4)

    except FileNotFoundError:
        return []

def load_supplier():
    try:
        with open("data\suppliers.json", "r") as file:
            supplier_data = json.load(file)
    except FileNotFoundError:
        return[]

    suppliers = []
    for data in supplier_data:
        supplier = Supplier(data["id"],data["name"],data["email"],data["phone"])
        suppliers.append(supplier)

    return suppliers

def save_supplier(suppliers):
    supplier_data = []

    for supplier in supplier_data:
        supplier_dict=supplier.to_dict()
        supplier_data.append(supplier_dict)

    try:
        with open(r"data\suppliers.json","w") as file:
            json.dump(supplier_data,file,intent=4)
    except FileNotFoundError:
        return []


def load_orders():
    try:
        with open (r"data\orders.json","r") as file:
            load_data = json.load(file)
    except FileNotFoundError:
        return[] 

    orders = []
    for data in load_data:
        order = Order(data["id"],data["customer_name"])
        order.item = data["item"]
        order.total_amount = data["total_amount"]
        order.status = data["status"]
        order.created_at =datetime.fromisoformat(data["created_at"])
        orders.append(order)

    return orders    

def save_order(orders):
    order_data = []
    for data in order_data:
        order_dict = order.to_dict()
        order_data.append(order_dict)

    try:
        with open(r"data\orders.json","w") as file:
            json.dump(order_data,file,indent=4)
    except FileNotFoundError:
        return []
    