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

def generate_report(total_units,failed_attempts,current_total):
   print("current orders:", current_total)
   print("Total units processed:", total_units)
   print("Failed attempts:", failed_attempts)

def load_inventory():
    orders = []

    while True:
        product_name = input("enter product name:")
        orders.append(product_name)
        if product_name == "stop": 
            break
        product_quantity = get_valid_input("enter product quantity:")
        if product_quantity is None:
            break
        orders.append(product_quantity)
        print("New order added:")
        print(product_name, product_quantity)

    return orders

def save_inventory(orders):
    with open("orders.txt", "w") as file:
        for order in orders:
            file.write(str(order) + "\n")


orders = []
current_total = 0
stock_quantity = 0
walk_circle = 0
failed_attempts = 0
inventory = load_inventory()
walk_circle += 1
current_total = calculate_tax(process_delivery(current_total, stock_quantity))
print("final inventory:",stock_quantity)
generate_report(stock_quantity, failed_attempts, current_total)
save_inventory(orders)
print("Order successfully saved to orders.txt")
