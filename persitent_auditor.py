def calculate_tax(original_price): 
    return original_price * (1+0.10)

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
    id = 1001
    orders = [id]

    while True:
        product_name = input("enter product name(or 'stop' to finish):")
        orders.append(product_name)
        if product_name == "stop": 
            break
        product_quantity = get_valid_input("enter product quantity:")
        if product_quantity is None:
            break
        orders.append(product_quantity)
        print("New order added:")
        print(id, product_name, product_quantity)
        id += 1
    return orders


def save_inventory(orders):
    with open("orders.txt", "w") as file:
        file.writelines(orders)

failed_attempts = 0
generate_report()
inventory = load_inventory()
generate_report()
save_inventory(inventory)
orders = []
print("Order successfully saved to orders.txt")
