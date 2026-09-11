stock_quantity = 0
walk_circle = 0
for walk_circle in range(111111):
 user_input = input("enter a stock quantity:")
 if user_input == "stop":
  break
 if user_input.isdigit() == False:
  print("ERROR:the quantity is not a number")
  continue
 stock_quantity_add = int(user_input)
 if stock_quantity_add < 0:
   print("ERROR:the quantity is negative")
   continue
 stock_quantity_add = int(user_input)
 stock_quantity += stock_quantity_add
 print("total inventory:",stock_quantity)
 walk_circle += 1
print("final inventory:",stock_quantity)



 

