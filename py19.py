#Make a program that produce the following output.
grocery_names = ["apple", "banana", "orange", "grapes",
"tomato", "potato", "milk", "bread", "butter"]
grocery_prices = [0.99, 0.5, 0.75, 2.99, 1.49, 0.99, 3.99, 2.49, 4.99]
#make vaiable for store index
index = 0
#print message for crocery list 
print("Crocery List:\nItems    |      price\n----------------------")
#initialize for loop for names 
for items in grocery_names:
#print result    
    print(f"{items} ------->    {grocery_prices[index]} $")
#increment one in the index   
    index+=1
#second way 
print("_"*30)
print("Crocery List:\nItems    |      price\n----------------------")
# initialize for loop with range 
for i in range(len(grocery_names)):
      print(f"{grocery_names[i]} ------->    {grocery_prices[i]} $")  
#third way 
#for foruit, prices in zip(grocery_names,grocery_prices):       
print("Crocery List:\nItems    |      price\n----------------------")
#initialiaze for loop with zip 
for  items, prices in list(zip(grocery_names,grocery_prices)):
    print(f"{items} ------->    {prices} $") 