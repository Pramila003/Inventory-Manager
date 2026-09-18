from models import Product

def find_product_by_id(produts,product_id):
    for product in produts:
        if product.id==product_id:
            return product
    return None

def display_product(product):
    print("ID:",product.id)
    print("name:",product.name)
    print("category",product.category)
    print("Price",product.price)
    print("quantity",product.quantity)
    print("supplier_id",product.supplier_id)
    print("reoder_level",product.reorder_level)

    
    if Product.is_low_stock():
        print("LOW STOCK")

def add_product(products, suppliers):
    product_id=int(input("enter product id"))
    name=input("enter product name")
    category=input("enter the category of product")
    price=int(input("enter th price"))
    quantity=int(input("enter the quantity"))
    supplier_id=int(input("enter supplier id"))
    reorder_level=int(input("enter reodrder level"))

    existing_product=find_product_by_id(products,product_id)

    if existing_product is not None:
        print("product already exist in list")

    supplier_found=False
    for supplier in suppliers:
        if supplier.id == supplier_id:
            supplier_found=True
            break
    if supplier_found is False:
        print(" supplier aid dose not exist,first add supplier id")


    new_product=Product(product_id,name,category,price,quantity,supplier_id,reorder_level)
    products.append(new_product)
    print("product added successfully")

def view_products(products):
    if len(products)==0:
        print("No product available")
        return

    print("all product")
    for product in products:
        display_product(product)


def search_product(products):
    print("product search by")
    print("1.ID")
    print("2.name")
    print("3.category")

    choice=int(input("enter choice"))
    if choice==1:
        product_id =int(input("enter product ID"))
        product=find_product_by_id(products,product_id)
        if product is not None:
            display_product(products)
        else:
            print("product not found")

    elif choice==2:
        name=input("enter product name").lower()
        found=False
        for name in products:
            if name in products.name.lower():
                display_product(products)
                found=True
        if found is False:
            print("product name does not exits")

    elif choice==3:
        category=input("enter category").lower()
        found=False
        for category in products:
            if category in products.category.lower():
                display_product(products)
                found=True
        if found is False:
            print ("product category does not exits")
    else:
        print("invalid choice")

def update_product(products,suppliers):
    product_id=int(input("enter the product is which you want to update"))
    product=find_product_by_id(products,product_id)
    if product is  None:
        print("product id does not exits")
    else:
        print("what wants to change")
        print("1.Name")
        print("2.Category")
        print("3.price")
        print("3.supplier ID")
        print("3reorder level")

        choice=int(input("enter the choice"))
        if choice==1:
            print("current name:",products.name)
            new_name=input("enter new name")
            if new_name.strip()=="":
                print("name can not be empty")
                return
            Product.name=new_name
            print("product name updated")


        elif choice==2:
            print("current category: ",products.category)
            new_category=input("enter new category")
            if new_category.strip()=="":
                print("category can not be empty")
                return
            Product.category=new_category
            print("category updated")

        elif choice==3:
            print("current price: ",products.price)
            new_price=input("enter new price")
            if new_price.strip()=="":
                print("price can not be empty")
                return
            Product.price=new_price
            print("price updated")

        elif choice==3:
            print("current supplier_id: ",products.supplier_id)
            new_supplier_id=input("enter new supplier_id")
            if new_supplier_id.strip()=="":
                print("supplier_id can not be empty")
                return
            products.supplier_id=new_supplier_id
            print("supplier_id updated")

        elif choice==4:
            print("current reorder_level: ",products.reorder_level)
            new_reorder_level=input("enter new reorder_level")
            if new_reorder_level.strip()=="":
                print("reorder_level can not be empty")
                return
            products.reorder_level=new_reorder_level
            print("reorder_level updated")

def restock_product(products):
    product_id=int(input("enter the product_id"))
    product=find_product_by_id(products,product_id)
    if product is None:
        print("product does not exits")
        return
    else:
        print("current_quantity: ",products.quantity)
        print("choose 1: to add " \
        "choose 2: to remove")
        choice=int(input("enter choice"))
        if choice==1:
            amount=input("enter new quantity")
            new_product_quantity=products.update_stock(amount)
            print(new_product_quantity)
        elif choice==2:
            amount=input("enter new quantity")
            new_product_quantity=products.update_stock(amount)
            print(new_product_quantity)

def remove_product(products):
    product_id=int(input("enter the product id"))
    product=find_product_by_id(products,product_id)
    if product is None:
        print("product does not exits")

    product_remove=input("are your sure you want to remove the product")
    if product_remove=='yes':
        products.remove(product)
    else:
        print("product is not remove ")

def show_low_stock_product(products):
    low_stock_products=[]
    for product in products:
        low_stock_products=product.is_low_stock()
        if low_stock_products:
            Product.append(low_stock_products)
    if len(low_stock_products)==0:
        print("All products have healthy stock")
    else:
        print(" display every product in low_stock_products")

def inventory_menu(products,supplier):
    print("Show inventory choices")
    print("1: add product/n 2: view_products/n 3:search_product/n 4: update_product/n 5: restock_product/n 6: remove_product/n 7: show_low_stock_products ")
    choice=int(input("enter the choice"))
    if choice==1:
        add_product(products, supplier)
    elif choice==2:
        view_products(products)
    elif choice==3:
        search_product(products)
    elif choice==4:
        update_product(products,supplier)
    elif choice==5:
        restock_product(products)
    elif choice==6:
        remove_product(products)
    elif choice ==7:
        show_low_stock_product(products)
    else:
        print("invalid syntax")
    

    


    

