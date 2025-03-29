#Do the following:  A. convert each inner list to a string and join them with a space and add them to a list named sentences. B. Make another list replace spaces with dashes and convert each word to uppercase. 
words = [["Hello", "from", "Codezilla"],      ["Python", "Course", "is", "awesome"],  
         ["I", "enjoy", "learning", "Python", "with", "You"]
         ] 
#make a list of sentences
sentences = []
#initialize for loop
for lst in words:
#convert each inner list to a string and join them with space    
    sentences.append(" ".join(lst))
#make a new list 
new_lst = []
#initialize for loop for words 
for word in sentences:
# replace dash  to space and convert to uppercases      
    new_lst.append( word.replace(" ","_").upper())    
#print result 
print(f" The list of sentence is : {sentences}")
print(f"The modified list of sentences is: {new_lst}")
