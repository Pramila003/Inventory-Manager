

def inventory_value_report(products):
    inventory_value = 0
    if not products:
        print("no product available")
        return 
    
    for product in products:
        product_value = product.quantity * product.price
        inventory_value += product_value

        print("product name", product.name)
        print("product quantity", product.quantity)
        print("product unit price", product.price)
        print("product value", product_value)

    print("overall inventory value",inventory_value)


def sales_report(orders):
    completed_orders_count = 0
    total_revenue = 0

    for order in orders:
        if order.status =="Completed":
            completed_orders_count +=1
            total_revenue +=order.total_amount

    if completed_orders_count == 0:
        print("No completed order")
        return

    average_order_amount = total_revenue / completed_orders_count

    print("complete order count",completed_orders_count)
    print("total_revnue",total_revenue)
    print("average_order_count",average_order_amount)


def top_selling_products(orders):
    product_sales={}

    for order in orders:
        if order.status == "Completed":

            for item in order.item:
                product_id = item["product_id"]
                product_name = item["product_name"]
                quantity = item["quantity"]

                if product_id not in product_sales:
                    product_sales[product_id] = {
                        "name": product_name,
                        "quantity" : 0
                    }

                product_sales[product_id]["quantity"] += quantity

def supplier_report(products, suppliers):
    if not suppliers:
        print("No supplier")
    for supplier in suppliers:
        print("Supplier name:",supplier.name)
        print("Supplier ID:",supplier.id)

    has_product=False

    for product in products:
        if product.is_low_stock():
            stock_state = "Low stock"
        else:
            stock_state = "Normal"
        print(product.name)
        print(product.quantity)
        print(product.price)
        print(stock_state)

        has_product = True
    if has_product is  False:
        print("No product assigned to this supplies")



def reports_menu(products, suppliers, orders):
    while True:
        print("1. Inventory value report")
        print("2. Sales report")
        print("3. Top-selling products")
        print("4. Supplier report")
        print("5. Return to main menu")
        choice = int(input("enter choice"))

        if choice == 1:
            inventory_value_report(products)

        elif choice == 2:
            sales_report(orders)

        elif choice == 3:
            top_selling_products(orders)
        elif choice == 4:
            supplier_report(products,suppliers)
        elif choice == 5:
            reports_menu
        else:
            print("invalid choice")

