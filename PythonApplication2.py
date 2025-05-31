#print the pizza name and price in the follwing info pizzas :
#pizza to print:
#Pepperonie pizza 
#chicken pizza 
#Hawiian pizza
pizzas = {
    "Pepperonie Pizza": 100, 
    "Margherita Pizza": 90, 
    "Meet Lover": 80, 
    "Chicken Pizza": 70, 
    "cheese": 60, 
    "Veggie": 40, 
    "Hawiian": 90 
    }
#make list for pizza need 
pizzas_list = ["Pepperoni", "Chicken", "Hawiian"]
#initiliaze for loop for print all the pizzas and price 
for pizza in pizza_list:
    print(f"{pizza} : {pizzas[pizzas]}")
print("_"*40)    
#----------------------------------------------------------
#print the follwing drinks from the menu 
#Drinks to print:
#Coke 
#Mango Juice
#Tea 
#Coffee
drinks = {
    "Coke": 70, 
    "Mango Juice": 90, 
    "Tea": 30, 
    "Coffee": 20, 
    "Orange Juice": 80,
    "Pepsi": 90 
}
#make list of drinks
drinks_list = ["Coke", "Mango Juice", "Tea", "Coffee"]
#initialize for loop 
for drink in drinks_list:
    print(f"{drink} : {drinks[drink]}")
#--------------------------------------------------
#add the follwing desertes items in the resturent menu 
#Ice cram - 70
#Chocolate Cacke - 100
#Cheese Cacke - 80
#Brownie - 60
#Donuit - 50
menu = {
    "Cheese Pizza": 120, 
    "Viggie Pizza": 90, 
    "Hawaiian Pizza": 70, 
    "Coke": 40, "Sprite": 30, 
    "Fanta": 25
}
#make dictionary to add new items on it
new_items = {
    "Ice cram" :70,
    "Chocolate Cacke":100,
    "Cheese Cacke": 80,
    "Brownie" : 60,
    "Donuit" : 50
}
#initialize for loop for add items in the dect named menu
for item in new_items:
    menu[item] = new_items[item]
del(new_items)
print(menu)
print("_"*40)
#----------------------------------------------------------
#another solution 
desertes = {
    "Cheese Pizza": 120, 
    "Viggie Pizza": 90, 
    "Hawaiian Pizza": 70, 
    "Coke": 40, "Sprite": 30, 
    "Fanta": 25
}
#make new dictionary to add new item on it 
new_desertes = {
    "Ice cram" :70,
    "Chocolate Cacke":100,
    "Cheese Cacke": 80,
    "Brownie" : 60,
    "Donuit" : 50
}
#add the new dictionary in the origenal dictonary(desertes)
desertes.update(new_desertes)
print(desertes)
del(new_desertes)
#print(new_desertes)
print("_"*40)
