#program print the total of numbers that are divisible by 3 and 7, and between 1 to 2000.  
number = 1
while number<2000:
    if number%3 == 0 or number%7 == 0:
      print(number)
    number += 1
      