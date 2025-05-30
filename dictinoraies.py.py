
#greate dictinoraiy called fruit and contains the following informations
#Apple
#Banana
#strawberry
#Mango 
fruits = {"Apple": 20, "Banana": 15, "Strawberry": 30, "Mango": 34}
print(fruits)
#----------------------------------------------------------------------
#greate dictionary called students contanis the follwing information 
#Aymen - 80
#Salim - 90
#Yasser - 96
students = {"Aymen":80, "Salim":90, "Yasser":96}
print(students)
#-----------------------------------------------------------------------
#greate dictionary called drinks contains the follwing information 
#Sprite - 20
#Coke - 30
#Nakhal  - 10
drinks = {"Sprite": 20, "Coke": 30,"Nkhla":10}
print(drinks)
#-----------------------------------------------------------------------
#greate dictionary called students_grades contains following information
#the key is the order and the values is the name of students 
#1 - Ahmed
#2 - Mohamed 
#3 - Salim
students_grades  = { 1:"Ahmed", 2 :"Mohamed", 3: "Salim"}
print(students_grades)
#------------------------------------------------------------------------
#Debug the following code, keeping the first and last names separated.
grades = {
("Ahmed", "Hassan"): 87,
("Hossam", "Ali"): 90,
("Mohamed", "Kamel"): 74,
("Ali", "Hamed"): 100,
("Ahmed", "Khaled"): 95
}
print(grades)
#------------------------------------------------------------------------
#print the prices of the follwing items 
#Peperonie Pizza 
#Chicken Pizza
#Hawaiian Pizza 
pizzas = {"Margaritha": 100,
          "Pepperonie": 140,
          "Meat lover":130,
          "Chicken": 80,
          "Cheese":90,
          "veggie": 125,
          "Hawaiian": 160,
          }
print(pizzas["Pepperonie"])
print(pizzas["Chicken"])
print(pizzas["Hawaiian"])
#---------------------------------------------------------------------------
#print the prices of the following drinks 
#Coke 
#mango juice 
#Tea 
#Coffee
drinks = {
    "Coke": 25,
    "Mango juice": 30,
    "Coffee": 20,
    "Tea":10
    }
print(drinks["Coke"])
print(drinks["Mango juice"])
print(drinks["Tea"])
print(drinks["Coffee"])
#-----------------------------------------------------------------------------
#Add the follwing desserts to the menu and update price of Hawaiian Pizza to 190 
#ice crame - 120
#chocolat cake": 50,
# Brownie - 40
# Donut - 30
menu = {  
    "Veggie Pizza": 67,
    "Hawaiian Pizza":190,
    "Coke": 30,
    "Sprite": 78,
    "Pepsi": 20,
    "Fanta": 15,
    }
menu["Hawaiian Pizza"] = 190
menu["ice Cram"] = 120
menu["Chocolat Cake"] = 90
menu["Chees Cake"] = 100
menu["Browine"] = 40
menu["Donut"] = 30
print(menu)
#------------------------------------------------------
#Print the prices of Soda items from the menu 
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
for drink in drinks:
    print(f"{drink}: {drinks[drink]}")
#-----------------------------------------------------
#Print available pizzas and their prices for the customer.
# Available Pizzas:
pizzas = {"Margherita": 100, "Pepperoni": 120, "Meat Lovers":
150, "Chicken": 130}
for pizza in pizzas:
    print(f"{pizza}: {pizzas[pizza]}")
#------------------------------------------------------------
students = {
    "Ahmed":{
        "grades":{
            "math": 100, 
            "arabic": 100, 
            "history": 90
            }, 
        "age": 20},
    "Salim":{
         "grades":{
            "math": 95, 
            "arabic": 100, 
            "history": 80
            }, 
        "age": 22},
        
    }
print(students["Salim"]["grades"]["arabic"])
