#Make a store program, with an extra print statement, before the totalorder coset, 
#showing the total cost for each item in list in descending order
#list to store prices
total_cost = []
#repeat the folowing steps unitli the user enter "done" or press Enter 
while True:
#read the product name    
    product_name = input("Eneter product name: ")
#if user enter "done" or press Enter then quite the programe     
    if product_name.lower() == "done" or len(product_name) == 0:
        break
#read the quantity    
    quantity = int(input("Enter quantity: "))
#read the price     
    price = float(input("Enter price: "))
#calculate the total items cost    
    total_items_cost = (quantity*price)
#add the total items cost in the list     
    total_cost.append(total_items_cost)           
#print the product name, quantity , price, total items cost    
    print("_"*30)
    print(f"Product: {product_name}\nquantity: {quantity}\nPrice: {price} $")
    print("_"*30)
    print(f"Total items cost: {total_items_cost} $")
    print("_"*30)                    
#print the thank you message 
print("Thank you for shopping with Salahshop. Have a great day!\nPrices in descending order:")
#sort the list prices in descending order and print it 
total_cost.sort(reverse=True)  
index = 0 
while index< len(total_cost):
    print(f"price {index+1}: {total_cost[index]} $")
    index += 1
#calculate the total cost of all items  
print("_"*30)  
print(f"Total cost is : {sum(total_cost)} $")    
     
              
