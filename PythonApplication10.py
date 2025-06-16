#make program that allow restaurent onwner to delet item from menu 
menu = {
    "Margherita Pizza": 100,
    "Pepperoni Pizza": 120,
    "Meat Lovers Pizza": 150, 
    "Chicken Pizza": 130,
    "Beef Burger": 100, 
    "Chicken Burger": 80
}
#initialize loop 
while True:
#get input from user     
    item = input("Enter the name of item you want to delet(press onter to exit): ").lower().title()
#check lenght of item
    if item=="":
        break
    elif item in menu:
#get input from user     
        message = input(f"Are you sue you want to delet the {item} ? (y/n): ").lower()
#check if message equal true     
        if message=="y":
#delet item from menu       
            del(menu[item])
            #menu.remove(menu[item])
            print("The item has deleted succesfuly")
    else:
        print("Not found")
print("The new menu is: ")
#initializ for loop 
for item,price in menu.items():
    print(f"{item}: {price:.2f} DA")


