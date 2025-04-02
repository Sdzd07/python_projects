#Find the smallest number in the following list without using min and sort. . 
numbers = [-588, -479, -713, -701, -885, -578, -835, -466, -935, -665, -360, -837, -389, -367, -454, -668, -907, -822, -541, -680,
           -405, -330, -625, -916, -331, -876, -689, -753, -810, -648, -787, -952, -718, -401, -502, -699, -533, -450, -580, -725
          ] 
#make a variable 
num = numbers[0]
#initialiaze for loop numbers
for number in numbers:
#check if number greater than num     
    if number>num:
        num = number
#print result 
print(num)        