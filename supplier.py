from models import Supplier
from validators import validate_email

def find_suppplier_by_id(suppliers, supplier_id):
    for supplier in suppliers:
        if supplier.id == supplier_id:
            return supplier
        else:
            return None

def display_supplier(supplier):
    print("Supplier ID",supplier.id)
    print("Name",supplier.name)
    print("Email",supplier.email)
    print("phone",supplier.phone)


def add_supplier(suppliers):
    supplier_id = int(input("enter the supplier id"))
    name = input("enter the name")
    email = input("enetr the email")
    phone = input("enter the phone")

    for supplier in suppliers:
        if supplier.id == supplier_id:
            print("Supplier ID alredy exits")
            return

    if name.strip() == "":
        print("name can not be empty")
        return 

    valid_email = validate_email(email)
    if email != valid_email:
        print(" email is invalid")
        return 

    supplier = Supplier(id , name, email, phone)
    suppliers.append(supplier)
    print("Supplierd  added successfully")

def view_suppliers(suppliers):
    if not suppliers:
        print("No supplier available")

    for supplier in suppliers:
        display_supplier(supplier)

def search_supplier(suppliers):
    supplier_id = int(input("enter supplier id you want to search"))
    find_suppplier_by_id(suppliers,supplier_id)

    supplier_name = input("enter supplier name you want to search").lower()
    for supplier in suppliers:
        if supplier.name.lower() == supplier_name:
            return supplier

def update_supplier(suppliers):
    suplpier_id = int(input("enter the suppplier id youe want to update"))
    supplier = find_suppplier_by_id(suppliers,suplpier_id)

    if supplier is None:
        print("now supplier exits:",suplpier_id)

    else:
        print("what you want to upadte")
        print("name")
        print("email")
        print("phone")
        choice = int(input("enter the choice"))

        if choice == 1:
            print("current name",Supplier.name)
            new_name = input("enter new name")
            if new_name.strip() == "":
                print("name can not be empty")

            supplier.name = new_name
            print("updated name:",supplier.name)

        if choice == 2:
            print("current email: ",supplier.email)
            new_email = input("enter new email")

            if not validate_email(new_email):
                print("email is onvalid")

            supplier.email == new_email
            print("updated email:",supplier.email)


def remove_supplier(suppliers):
    supplier_id = input(" enter supplier id you want to remove")
    supplier = find_suppplier_by_id(suppliers,supplier_id)

    if supplier is None:
        print("supplier does not exits")
        return
    else:
        display_supplier(suppliers)
        comfirm_del = input(" delete this supplier(y/n)").lower()
        if comfirm_del == 'y':
            suppliers.remove(supplier)
            print("delete supplier")
        else:
            print("did not delete")

def supplier_menu(suppliers):
    while True:
            print("1. Add supplier")
            print("2. View suppliers")
            print("3. Search supplier")
            print("4. Update supplier")
            print("5. Remove supplier")
            
            choice = input("Enter your choice: ")
            
            if choice == 1:
                add_supplier(suppliers)
            elif choice == 2:
                view_suppliers(suppliers)
            elif choice == 3:
                search_supplier(suppliers)
            elif choice ==4:
                update_supplier(suppliers)
            elif choice == 5:
                remove_supplier(suppliers)
            else:
                print("invalid choice")
