#Using For loop search for the word that the user will enter in the following list and print the result. 
words = [ 'each', 'those', 'feel', 'seem', 'high', 'place', 'little', 'world', 'very', 'still',         
          'nation', 'hand', 'life', 'tell', 'write', 'become', 'here', 'show', 'house', 'both',        
          'between', 'need', 'mean', 'call', 'develop', 'under', 'last', 'right', 'move', 'thing',       
          'general', 'school', 'never', 'same', 'another', 'begin', 'while', 'number', 'part',       
          'turn', 'real', 'leave', 'might', 'want', 'point', 'form', 'child', 'small', 'since',       
          'against', 'late', 'home', 'interest', 'large', 'person', 'open', 'public', 'follow',       
          'during', 'present', 'without', 'again', 'hold', 'govern', 'around',        
          'head', 'consider', 'word', 'program', 'problem', 'however', 'lead', 'system',         
          'order', 'plan', 'keep', 'face', 'group', 'play', 'stand', 'increase',        
          'early', 'course', 'change', 'help', 'line', 'possible', 'fact', 'down'
        ]
#get input from user 
message = input("Enter the word search for: ").lower()
word_found = "not found"
#initialize for loop 
for word in words:
#check if word equal user input   
    if word == message:
       word_found = word 
if word_found!= "not found":        
#print result     
    print("The word found in the list")
else:    
    print(f"The word not found")    
