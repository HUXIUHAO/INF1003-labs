def calculate_tax(original_price): 
    return original_price * (1+0.10)

def count_orders():
    try:
        with open("orders.txt", "r") as file:
            order_lines = file.readlines()
            return len(order_lines)
    except FileNotFoundError:
        return 0

def process_delivery(current_total, new_value):
    return current_total + new_value 

def get_valid_input(prompt):
    failed_attempts = 0
    while True:
        user_input = input(prompt)
        if user_input == "stop":
            return None
        if not user_input.isdigit():
            print("ERROR: the quantity is not a number")
            failed_attempts += 1
            continue
        stock_quantity_add = int(user_input)
        if stock_quantity_add < 0:
            print("ERROR: the quantity is negative")
            failed_attempts += 1
            continue
        if stock_quantity_add == 0:
            print("ERROR: the quantity is zero")
            failed_attempts += 1
            continue
        return stock_quantity_add

def generate_report():
   with open("orders.txt", "r") as file:
    order_lines = file.readlines()
    print("current orders:")
    for line in order_lines:
        print(line.strip())


def load_inventory():
    id = count_orders() + 1001
    orders = [id]

    product_name = input("enter product name(or 'stop' to finish):")
    if product_name.lower() == "stop":
        return None
    orders.append(product_name)
    product_quantity = get_valid_input("enter product quantity:")
    if product_quantity is None:
            print("No quantity entered. Exiting.")
    else:
        orders.append(product_quantity)
        print("New order added:")
        print(id, product_name, product_quantity)
    order_string = f"{id},{product_name},{product_quantity}\n"
    return order_string


def save_inventory(order_string):
    if order_string is not None:
     with open("orders.txt", "a") as file:
        file.writelines(order_string)
    else:
        print("No order to save.")

failed_attempts = 0
while True:
 generate_report()
 inventory = load_inventory()
 generate_report()
 if inventory is not None:
  save_inventory(inventory)
  orders = []
  print("Order successfully saved to orders.txt")
 else:
    break
