#Print the total of the even numbers that the user will Enter.  
#get input from user 

even_number = 0
while True:
    number = input("Enter number: ")
    if number == "done":
        break 
    elif int(number)%2 == 0:
        print(number)