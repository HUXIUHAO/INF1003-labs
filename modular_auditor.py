
def calculate_tax(original_price): 
    return original_price * (1+0.10)
def process_delivery(current_total, new_value):
    return current_total + new_value 
def get_valid_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input == "stop":
            return None
        if not user_input.isdigit():
            print("ERROR: the quantity is not a number")
            fail += 1
            continue
        stock_quantity_add = int(user_input)
        if stock_quantity_add < 0:
            print("ERROR: the quantity is negative")
            fail += 1
            continue
        return stock_quantity_add
def generate_report(total_units,fail,current_total):
   print("current total after tax:", current_total)
   print("Total units processed:", total_units)
   print("Failed attempts:", fail)    
current_total = 0
stock_quantity = 0
walk_circle = 0
fail: int = 0
for walk_circle in range(111111):
 user_input = get_valid_input("enter a stock quantity:")
 if user_input is None:
     break
 stock_quantity_add = int(user_input)
 stock_quantity += stock_quantity_add
 print("total inventory:",stock_quantity)
 walk_circle += 1
current_total = calculate_tax(process_delivery(current_total, stock_quantity))
print("final inventory:",stock_quantity)
generate_report(stock_quantity, fail, current_total)



 