#incarse the peice of pizzas by 20 percent then print the items of menu
menu = {
"Cheese pizza": 100,
"Veggie pizza": 120,
"Hawaiian pizza": 150,
"Coke": 30,
"Sprite": 25,
"Fanta": 25,
"Pepsi": 30
}
#initializ for loop to edit price of each value on the menu 
for price in menu:
#chek if pizza in the menu    
    if "pizza" in menu:
    menu[price] = f"{menu[price]*1.2:.2f}"
print(f"{menu}")
#other solution 
menu_ = {
"Cheese pizza": 100,
"Veggie pizza": 120,
"Hawaiian pizza": 150,
"Coke": 30,
"Sprite": 25,
"Fanta": 25,
"Pepsi": 30
}
for item, price in menu_.items():
     menu_[item] = f"{price*1.2:.2f}"
     if "pizza" in menu:
print(menu_)
#for print each item in line 
#initiliaz for loop
for item in menu_:
    print(f"{item} : {menu_[item]}")
#Print soda items from the following menu.
drinks = {
"Latte": 30,
"Coke": 30,
"Sprite": 25,
"Fanta": 25,
"Pepsi": 30,
"Tea": 20,
"Coffee": 25,
"Orange Juice": 30,
"Mango Juice": 30
}
soda_drinks = ["Coke", "Sprite", "Fanta", "pepsi"]
for drink in soda_drinks:
    print(f"{drink} cost : {drinks[drink]}")
#other solution 
for drink, price in drinks.items():
    if drink in soda_drinks:
        print(f"{drink} cost : {price}")



