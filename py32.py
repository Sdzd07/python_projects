#Modify this list of words to make All words are uppercase. # list of words 
words = [         
    'have', 'that', 'they', 'with', 'this', 'from', 'which', 'would', 'will', 'there',         
    'make', 'when', 'more', 'other', 'what', 'time', 'about', 'than', 'into', 'could',          
    'state', 'only', 'year', 'some', 'take', 'come', 'these', 'know', 'like', 'then',         
    'first', 'work', 'such', 'give', 'over', 'think', 'most', 'even', 'find', 'also',         
    'after', 'many', 'must', 'look', 'before', 'great', 'back', 'through', 'long',         
    'where', 'much', 'should', 'well', 'people', 'gouda', 'just', 'because', 'good',          
    'each', 'those', 'feel', 'seem', 'high', 'place', 'little', 'world', 'very', 'still',          
     'nation', 'hand', 'life', 'tell', 'write', 'become'       
        ] 
#make all words to uppercase and add them in the list 
uppercase_words = [word.upper() for word in words]
#print uppercse words 
print(", ".join(uppercase_words))
#another way for print the uppercase words 
print(*uppercase_words, sep=", ")
#Edit words list to gain the following outputs. 
words = [["Hello", "from", "Codezilla"],  ["Python", "Course", "is", "awesome"],  ["I", "enjoy", "learning", "Python", "with", "Codezilla"]] 
modify_list = [" ".join(sentence) for sentence in words ]
print(modify_list)
