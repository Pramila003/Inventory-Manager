
from datetime import datetime

class Product:
    def __init__(self,id,name,category,price,quantity,supplier_id,reorder_level):
        self.id=id
        self.name=name
        self.category=category
        self.price=price
        self.quantity=quantity
        self.supplier_id=supplier_id
        self.reorder_level=reorder_level

    def update_stock(self,amount):
        self.amount=amount
        if (amount>0) :
            self.quantity =self.amount
        else:
            self.quantity=0

    def is_low_stock(self):
        if (self.quantity <= self.reorder_level):
            return True
        else:
            return False
        
    def to_dict(self):
        return{
            "id": self.id,
            "name": self.name,
            "category": self.category,
            "price": self.price,
            "quantity": self.quantity,
            "supplier_id": self.supplier_id,
            "reorder_level":self.reorder_level
        }


class Supplier:
    def __init__(self,id,name,email,phone):
        self.id=id
        self.name=name
        self.email=email
        self.phone=phone 

    def to_dict(self):
            return{
                "id": self.id,
                "name": self.name,
                "email": self.email,
                "phone": self.phone
            }

class Order:
    def __init__(self,id,customer_name):
        self.id=id
        self.customer_name=customer_name
        self.items=[]
        self.total_amount=0
        self.status= "Pending"
        self.created_at=datetime.now()

    def add_item(self,product,quantity):
        subtotal=product.price *quantity
        item={
             "product_id": product.id,
             "product_name":product.name,
             "quantity":quantity,
             "unit_price":product.price,
             "subtotal":subtotal
        }
        self.items.append(item)
        self.total_amount += subtotal

    def calculate_total(self):
         total=0
         for item in self.items:
              total +=item["subtotal"]
         self.total_amount += total
         return self.total_amount

    def change_status(self,new_status):
         alllowed_status=["Pending","Completed","Cancelled"]
         if new_status in alllowed_status:
              self.status=new_status
              return True
         return False
        

    def to_dict(self):
            return{
                "id": self.id,
                "customer_name": self.customer_name,
                "items": self.items,
                "total_amount": self.total_amount,
                "status":self.status,
                "created_at":self.created_at
               
            }
