#Sum the even numbers between 28 and 928 in at least 3 different ways. 
total = 0
for i in range(28,929,2):
    total+= i
print(f"{total}\n-------------------------------")  
#####################################################
total = []
for i in range(28,929,2):
    total.append(i)
print(f"{sum(total)}\n--------------------------")    
#####################################################
total = 0
for i in range(28,929):
    if i%2==0:
        total+=i
print(f"{total}\n-------------------------------") 
####################################################
total = 0
rng = range(28,929)
for i in rng:
    if i%2==0:
        total+=i
print(f"{total}\n-------------------------------") 
################################################       
#Print the following list in the following form. .
fruits = ['apple', 'banana', 'orange', 'grape', 'mango']
print("The avaible fruits :")
for i in range(len(fruits)):
    print(f"{i+1} . {fruits[i]} ")
