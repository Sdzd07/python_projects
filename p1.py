#Find the total of the numbers in the list. 
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
total = 0
for number in numbers:
    total+=number 
print(f"The total is: {total}")
print("_"*30)
#Print the characters of the following string, each on a line. 
string = "Python Course" 
for character in string:
    print(character)
print("_"*30)
#Print the total cost of the following list.
prices = [10.99, 9.99, 15.99, 7.99, 12.99] 
total_cost = 0
for price in prices:
    total_cost +=price
print(f"The total cost is: {total_cost} dollares")
print("_"*30)
#Print the multiplication result of the following list. 
numbers = [1, 2, 3, 4, 5] 
total = 1
for number in numbers:
    total*=number
print(f"Multiplicatino result is: {total}")    
#Find the square of the numbers in the list.
#make list 
print("_"*30)
numbers =[1, 2, 3, 4, 5]
for number in numbers:
    square_num = number**2
    print(f"square of the {number} is: {square_num}") 
print("_"*30)
#Find the product of numbers that user enters. 
#get input from use
list_num = []
while True:
    number = float(input("Enter number (0 to stop): "))
    if number == 0:
        break
    list_num.append(number)
total = 1
for num in list_num:
       total*=num
print(f"The product of the numbers in {list_num} is {total:,.2f}")        