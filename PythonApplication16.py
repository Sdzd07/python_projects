#make pharmacy managment program that intract with user
inventory = {"Paracetamol": {"price":25, "quantity":10},
"Aspirin": {"price":15, "quantity":20},
"Ibuprofen": {"price":20, "quantity":15},
"Cough Syrup": {"price":30, "quantity":5},
"Augmentin": {"price":100, "quantity":7},
"Amoxicillin": {"price":80, "quantity":8},
"Panadol": {"price":25, "quantity":10},
"Zinc": {"price":15, "quantity":20},
"Vitamin C": {"price":20, "quantity":15},
"Fucidin": {"price":30, "quantity":5},
"Kolanog": {"price":100, "quantity":2}
}
options = '''1-Add new items 
2-Remove items 
3-update items
4-Check ivailable quantity 
5-Print treatment information
6-Exit'''
#initializ while loop
while True:
    print(options)
    choice_number = input("Enter your choice: ")
    if choice_number=="1":
        while True:
            print("------Adding new items------")
            new_item = input("Enter the name of new item (prees enter to exit): ").lower().title()
            if new_item=="":   
                break   
            price = float(input("Enter the price:"))
            quantity = int(input("Enter the quantity:"))
            inventory[new_item] = price
            print("The item was added successfuly")      
    elif choice_number=="2":
        while True:
            print("------Deleted items------")
            item_name = input("Enter the name of item you want to deleted (prees enter to exit): ").lower().title()
            if item_name=="":     
                break
            elif item_name in inventory:
                double_check = input(f"Are you sure you want to delete {item_name} item (y/n): ")
                if double_check=="y":
                    del(inventory[item_name])
                    print("The item was deleted sucessfuly")
            else: 
                print("Item not found")            
    elif choice_number=="3":
        while True:
            item_name = input("Enter the name of item you want to update (press enter to exit): ").lower().title()
            print("------Update items------")
            if item_name=="":
                break
            elif item_name in inventory:   
                update_price = float(input("Enter new price (press enter to exit): "))
                update_quantity = int(input("Enter new quantity: "))
                inventory[item_name].update({"price":update_price,"quantity":update_quantity})
                print("The item was updated successfuly")
            else:
                print("Item not found")
    elif choice_number=="4":
        while True:
            print("------Chacking item quantity------")
            item_name = input("Enter the name of item (prees enter to exit): ").lower().title()
            if item_name=="":
                break
            elif item_name in inventory:
                quantity = inventory[item_name]["quantity"]
                print(f"We have {quantity} {item_name} units")
            else: 
                print("Item not found")
    elif choice_number=="5":
        while True:
            print("------Printing treatment information------")
            item_name = input("Enter the name of item (prees enter to exit): ").lower().title()
            if item_name=="":  
                break
            elif item_name in inventory:
                information_item = inventory[item_name]
                price = information_item["price"]
                quantity = information_item["quantity"]
                print(f"Item: {item_name}\nPrice: {price:.2f} DA\nQuantity: {quantity} units")
            else:
                print("Item not found")
    elif choice_number=="6":
        print("Have a nice day")
        break
    else:
        print("Invalid option")