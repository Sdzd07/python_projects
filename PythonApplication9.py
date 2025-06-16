#mak program that allow restaurent user owner to add new items to the menu
menu = {
    "Margaritha Pizza": 100,
    "Meat lover Pizza": 120,
    "Pepperonie Pizza": 125,
    "Chicken Pizza": 95
}
#initializ loop 
while True:
#get input from user (item)
    item = input("Enter the name of item (press enter to exit): ").lower().title()
    if len(item)==0:
        break
#get input from user (price of item)
    price = int(input("Enter the price:"))
#add the new item to the menu 
    menu[item] = price
#there are more solution to add new item to the menu:
    #menu.update({item:price})
print("The New Menu:")
for item,price in menu.items():
    print(f"{item}: {price:.2f} DA")
