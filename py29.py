#Write code to find the sum of numbers that are divisible by 3 and between 20 and 140 then print the numbers separated by a comma. 
#make list
list_numbers = [ num for num in range(20,141) if num%3==0]
#sum total_numbers that are divisible by 3
sum_number = sum(list_numbers)
#convert valaus into the list to string
str_list = [str(num)for num in list_numbers]
# print sum  of total_numbers that are divisible by 3
print(f"The sum of total numbers divisible by 3  is: {sum_number}")
#separate the numbers that are divisible by 3 by comma and print it 
print(f"The numbers are : {",".join(str_list)}")
#another way to print numbers and separate by comma 
print(*list_numbers,sep=",")