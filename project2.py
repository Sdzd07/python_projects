#program that prints the first multiple of 7 in the following list
index = 0
list_number = [953, 776, 532, 665, 973, 683, 484, 499, 741, 980]
while index<len(list_number):
    if list_number[index]%7!=0: 
        index+=1
    else:
        print(list_number[index]) 
        break   

    
    
    
          
