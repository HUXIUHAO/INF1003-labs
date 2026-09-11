stock_quantity = 0
walk_circle = 0
for walk_circle in range(111111):
 user_input = input("enter a stock quantity:")
 if user_input == "stop":
  break
 stock_quantity_add = int(user_input)
 stock_quantity += stock_quantity_add
 print("total inventory:",stock_quantity)
 if stock_quantity < 0:
  print("ERROR:the quantity is negative")


 

