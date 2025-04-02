#Debug the following code with at least 2 solutions, so that "Found Codezilla!" is the last printed output codezilla Found!
#first way 
nested_list = [["Hello", "from", "Codezilla"],["Python", "Course", "is", "awesome"],["I", "enjoy", "learning", "Python"]]  
lst_words = []
for lst in nested_list:     
    print(lst) # You can not remove this line
# You can not remove this line     
    for word in lst:         
        print(word)# You can not remove this line 
        lst_words.append(word)
# You can not remove this line         
if "Python" in lst_words:             
     print("Found Python!") 
     print("_"*20)# This should be the last line to be printed    
        
else: 
    print(f"Python word not found")
    print("_"*20)
        
#second way
nested_list = [["Hello", "from", "Codezilla"],["Python", "Course", "is", "awesome"],["I", "enjoy", "learning", "Python"]]  
for lst in nested_list:     
    print(lst) 
    for word in lst:          
            print(word) 
    if word.lower() == "python":                              
                print("_"*20)
                print("Found Python")
                break

    
