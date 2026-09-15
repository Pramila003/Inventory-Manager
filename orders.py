from models import Product
from inventory  import find_product_by_id
from models import Order
def find_order(orders,search_value):
    for order in orders:
        if order.id == search_value:
            return order
        if order.name.lower() == search_value.lower():
            return order
    return None

def add_product_to_order(order,produts):
    product_id=int(input("enter product id"))
    product_exist=find_product_by_id(produts,product_id)
    if product_exist is None:
        print("product does not exits")

    product_quantity=int(input("enter product quantity"))
    if product_quantity <=0:
        print("product can not be added")

    if product_quantity >  Product.quantity:
        print("Insufficient stock")

    Order.add_item(product,quantity)

def create_order(orders,products):
    order_id=int(input("enter product id"))
    existing_order=find_order(orders,order_id)
    if existing_order is not None:
        print("product already exits in Orders")
        return

    customer_name=input("enter customer name")
    if customer_name.strip():
        print("customer name can not be empty")
        return

    order=Order(order_id,customer_name)

    while True:
        add_product_to_order(order,products)
        choice=input("Add another product? yes/no").lower()
        if choice =='yes':
            break

        if not order.item :
            print("Order has no items. It was not saved.")
            return 

        order.calculate_total()
        orders.append(order)

        print("Order created successfully.")
        print("Order ID:", order.id)
        print("Total amount:", order.total_amount)
        print("Status:", order.status)

def process_order(orders,products):
    order_id=int(input("enter order id"))
    order=find_order(orders,order_id)
    if order is None:
        print("order not found")

    if order.status =="Completed":
        print("Order already processed")

    if order.status=="Cancelled":
        print("Cancelled orders cannot be processed")

    for item in order.item:
        product=find_product_by_id(products,item["product_id"])
        if product is None:
            print("product not found",item["product_id"])
            return
        if item["quantity"]> product.quantity:
            print("insufficient stock for",product.name)
            return

        for item in order.items:
            product = find_product_by_id(products, item["product_id"])

            product.update_stock(-item["quantity"])

        order.change_status("Completed")

        print("Order processed successfully.")
        print("Order ID:", order.id)
        print("Total amount:", order.total_amount)

def cancel_order(orders,products):
    order_id=input("enter the order id")
    order=find_order(orders,order_id)

    if order is None:
        print("order did not found")
        return

    if order.status =='Cancelled':
        print("Order is already cancelled")
        return

    if order.status=="Completed":
        for item in order.items:
            product=find_product_by_id(products,item["product_id"])
            product.update_stock(item["quantity"])

    order.change_status("Cancelled")
    print("Order cancelled successfully")


def view_orders(orders):
    for order in orders:
        if not  order:
            print("no order found")
            return

        print("all order")
        for order in orders:
            print("Order ID:", order.id)
            print("Customer:", order.customer_name)
            print("Status:", order.status)
            print("Created at:", order.created_at)
            print("Total amount:", order.total_amount)

        print("Items")
        for item in order.items:
            print("Order ID:", order.id)
            print("Customer:", order.customer_name)
            print("Status:", order.status)
            print("Created at:", order.created_at)
            print("Total amount:", order.total_amount)

            

def orders_menu(orders, products):
    while True:
        print("\n--- Order Management ---")
        print("1. Create order")
        print("2. Process order")
        print("3. Cancel order")
        print("4. View all orders")
        print("5. Find order")
        print("6. Return to main menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_order(orders, products)

        elif choice == "2":
            process_order(orders, products)

        elif choice == "3":
            cancel_order(orders, products)

        elif choice == "4":
            view_orders(orders)

        elif choice == "5":
            search_value = input("Enter order ID or customer name: ")
            order = find_order(orders, search_value)

            if order is None:
                print("Order not found.")
            else:
                print("Order ID:", order.id)
                print("Customer:", order.customer_name)
                print("Status:", order.status)
                print("Total:", order.total_amount)

        elif choice == "6":
            break

        else:
            print("Invalid choice.")

    

