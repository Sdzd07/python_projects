# program print the total of the numbers that the user will Enter. 
#get input from user 
total_nums = []
while True:
    number = input("Enter the number and when you finish write done: ")     
    total_nums.append(number)
    if number=="done".lower() or number=="done".upper():
        break
    print(sum(map(int,total_nums)))

#solution by another way
print("_"*50) 
total_nums = 0
while True:
    number = input("Enter the number and when you finish write done : ")     
    if number=="done".lower() or number=="done".upper():
        break
    print(total_nums+int(number))
   
