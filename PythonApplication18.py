#Make a program for DRF Cafe that interacts with the user like the following.
hot_drinks = {"Coffee": 20, "Tea": 15, "Hot Chocolate": 25}
cold_drinks = {"Soda": 10, "Iced Tea": 15, "Smoothie": 30}
desserts = {"Ice Cream": 50, "Chocolate Cake": 60,
"Cheesecake": 70}
menu = {"hot_drinks":hot_drinks, "cold_drinks":cold_drinks, "desserts":desserts}
print("Welcome to DRF Cafe")
order = {}
while True:
    for i, item_type in enumerate(menu):
        print(f"{i+1}. {item_type}")
    choice = input("Please, Enter the Number of the Item Type(Enter to exit): ")
    if choice == "":
        break
    item_type_name = list(menu)[int(choice) - 1]
    print(item_type_name)
    item_type = menu[item_type_name]
    for i, item in enumerate(item_type):
        item_price = item_type[item]
        print(f"{i+1}. {item}: {item_price} DA")
    choice = input("Enter Item Number: ")
    item_name = list(item_type)[int(choice) - 1]
    item_price = item_type[item_name]
    item_quantity = int(input("Please Enter Quantity: "))
    item_total = item_price * item_quantity
    order[item_name] = {"price": item_price, "quantity": item_quantity, "total": item_total}
total_orders = [order[item]["total"] for item in order]
total_orders_price = sum(total_orders)
print("-" * 20)
print("Your order is:")
print("-" * 20)
for item in order:
    item_info = f"""Item: {item}
    Price: {order[item]['price']} DA 
    Quantity: {order[item]['quantity']} units
    Total: {order[item]['total']} DA"""
    print(item_info)
    print("-" * 20)
print(f"Total Order: {total_orders_price} DA")

