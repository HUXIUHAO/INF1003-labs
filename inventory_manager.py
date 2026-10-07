def get_valid_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input == "stop":
            return None
        if not user_input.isdigit():
            print("ERROR: the quantity is not a number")
            continue
        stock_quantity_add = int(user_input)
        if stock_quantity_add < 0:
            print("ERROR: the quantity is negative")
            continue
        if stock_quantity_add == 0:
            print("ERROR: the quantity is zero")
            continue
        return stock_quantity_add

def add_product(inventory, product_id, product_name, product_price, product_stock):
    import json
    for product in inventory:
        if product['id'] == product_id:
            print(f"Product with ID {product_id} already exists. Cannot add duplicate.")
            return
        elif product['name'].lower() == product_name.lower():
            print(f"Product with name '{product_name}' already exists. Cannot add duplicate.")
            return
    new_product = {
         "id": product_id,
         "name": product_name,
         "price": product_price,
         "stock": product_stock
         }
    inventory.append(new_product)
    print("Product added successfully!")
    return inventory

def save_inventory(inventory):
    import json
    with open("inventory.json", "w") as f:
        json.dump(inventory, f)
    print("Inventory saved successfully to inventory.json.")

def load_inventory():
    import json
    try:
        with open("inventory.json", "r") as f:
            inventory_data = json.load(f)
        print("Inventory loaded successfully from inventory.json.")
        return inventory_data
    except FileNotFoundError:
        print("inventory.json not found. Starting with an empty inventory.")
        return []

def update_stock(inventory):
  import json
  print("Enter product ID to update stock:")
  product_id = get_valid_input("Enter product ID to update stock:(or 'stop' to finish)")
  if product_id is None:
      return
  for product in inventory:
      if product['id'] == product_id:
            print("product found:")
            print("name:", product['name'])
            print("current stock:", product['stock'])
            new_quantity = get_valid_input("Enter new stock quantity:")
            product['stock'] = new_quantity
            print(f"Product ID {product_id} stock updated to {new_quantity}.")
            return
  print(f"No product found with ID {product_id}.")

def search_product(inventory):
    import json
    search_name = input("Enter product ID to search:(or 'stop' to finish)")
    if search_name.lower() == "stop":
        return
    found = False
    for product in inventory:
        if product[0].lower() == search_name.lower():
            print(f"Found Product - ID: {product['id']}, Name: {product['name']}, Quantity: {product['stock']}")
            found = True
            break
    if not found:
        print(f"No product found with ID '{search_name}'.")

def display_all(inventory):
    with open("inventory.json", "r") as f:
        inventory_data = json.load(f)
    print("Displaying all products:")
    print(inventory_data)

import json
inventory_data = load_inventory()

print(".     ======  //   //   ======   ================================ ")                
print(".      //    //   //   //        --------------------------------  ")           
print(".     //    //===//   //====     <  INVENTORY  MANAGER  SYSTEM  >  ") 
print(".    //    //   //   //          -------------------------------- ")        
print(".   //    //   //   =======      ====================est.2026==== \n")   

print("-----------MENU-----------")
print("1. Display All Products")
print("2. Add Product")
print("3. Update Stock")
print("4. Search Product")
print("5. Save Inventory")
print("6. Exit")
print("---------------------------\n")

while True:
 option = input("Enter option:")
 if option == "1":
    display_all(inventory_data)
    continue
 elif option == "2":
    New_product = []
    product_name = input("Enter product name:")
    product_stock = get_valid_input("Enter product stock:")
    if product_stock is not None:
        new_product = add_product(New_product, len(inventory_data) + 1001, product_name, 0, product_stock)
        continue
    else:
        print("No stock entered. Product not added.")
        continue
    
 elif option == "3":
    update_stock(inventory_data)

 elif option == "4":
    search_product(inventory_data)

 elif option == "5":
    save_inventory(new_product)

 elif option == "6":
    print("Exiting the program.")
    break

