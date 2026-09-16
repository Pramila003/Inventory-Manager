
from orders import orders_menu
from storage import save_order,load_orders, save_supplier, load_products, save_products, load_supplier
from reports import reports_menu
from inventory import inventory_menu

def main():
    product = load_products()
    supplier = load_supplier()
    orders = load_orders()

    while True:
        print("1. Product management")
        print("2. Supplier management")
        print("3. Order management")
        print("4. Reports")
        print("5. Save and exit")

        choice = int(input("enter the choice"))
        if choice == "1":
            inventory_menu(products,suppliers)
        elif choice == "2":
            supplier_menu(suppliers)
        elif choice == "3":
            orders_menu(orders, products)
        elif choice =="4":
            reports_menu(products, suppliers, orders)
        elif choice =="5":
                save_products(products)
                save_supplier(suppliers)
                save_order(orders)

                print("Data saved. GoodBye!")
                break
        else:
            print("Invalid choice")

main()
