#Make a Pizza program that interact with the user in the following form. 
#a make a list of pizzas
pizzas = ['Margherita', 'Pepperoni', 'Super Supreme', 'Hawaiian', 'Meat Lovers', 'Cheese Lovers'] 
#print greating message 
print(f"Welcome to PL Pizzas\nWe have the follwing pizzas: ")
print("_"*30)
#intialize for loop 
for i in range(len(pizzas)):
    print(f"{i+1} .{pizzas[i]}")
#get input from user 
order_pizzas = int(input(f"Enter the number of pizza you want to order: "))
num_pizzas = int(input("Enter the number of pizzas you want: "))
#print result 
print("_"*30)
print(f"Thanks for choosing PL pizzas\nPlease, Enjoy your time! ")
print(f"while we get {num_pizzas} pizzas {pizzas[order_pizzas-1]} ready for you.")
