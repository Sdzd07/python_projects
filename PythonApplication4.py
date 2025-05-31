#Make a Pizza program that asks the user about the
#wanted pizza, and if available, it prints the pizza andits price. otherwise, you should print a sorry
pizzas = {"Margherita": 100, "Pepperoni": 120, "Meat Lovers": 150, "Chicken": 130}
#get input from user 
item = input("What pizza whould you want :").lower().title()
#chek if item is on pizzas dict
if item in pizzas:
    print(f"{item} pizza is avilaible, pice : {pizzas[item]:.2f}")
else:
    print(f"Sorry, {item} pizza not avilaible")
print("_"*40)
#Print the menu after increasing the prices by 20%.
pizzas_menu = {"Margherita": 100, "Pepperoni": 120, "Meat Lovers": 150, "Chicken": 130}
for pizza in pizzas_menu:
    price = pizzas_menu[pizza] 
     pizzas_menu[pizza] = f"{price*1.2:.2f}"   
print(pizzas_menu)
print("_"*40)
for item in pizzas_menu:
    print(f"{item} : {pizzas_menu[item]}")
#other solution
pizzas_menu_ = {"Margherita": 100, "Pepperoni": 120, "Meat Lovers": 150, "Chicken": 130}
for pizza, price in pizzas_menu_.items():
    pizzas_menu_[pizza] = f"{price*1.2:.2f}"
print("_"*40)
print(pizzas_menu_)
for pizza, price in pizzas_menu_.items():
    print(f"{pizza} : {price}")




