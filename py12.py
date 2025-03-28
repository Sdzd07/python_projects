# Make All the following list items uppercase.  
words = ['have', 'that', 'they', 'with', 'this', 'from', 'which', 'would', 'will', 
         'there', 'make', 'when', 'more', 'other', 'what', 'time', 'about', 'than', 
         'into', 'could', 'state', 'only', 'year', 'some', 'take', 'come', 'these', 
         'know', 'like', 'then', 'first', 'work', 'such', 'give', 'over', 'think', 
         'most', 'even', 'find', 'also', 'after', 'many', 'must', 'look',  'before', 
         'great', 'back', 'through', 'long', 'where', 'much', 'should', 'well', 'people',
           'gouda', 'just', 'because', 'good', 'each', 'those', 'feel', 'seem', 'high', 
           'place', 'little', 'world', 'very', 'still', 'nation', 'hand', 'life', 'tell', 
           'write', 'become', 'here', 'show', 'house', 'both', 'between', 'need', 'mean', 
           'call', 'develop', 'under', 'last', 'right', 'move', 'thing', 'general', 'school',
             'never', 'same', 'another', 'begin', 'while', 'number', 'part', 'turn', 'real', 'leave',
               'might', 'want', 'point', 'form', 'child', 'small', 'since', 'against', 'late', 'home', 
               'interest', 'large', 'person', 'open', 'public', 'follow', 'during', 'present', 'without', 
               'again', 'hold','govern', 'around', 'head', 'consider', 'word', 'program', 'problem',
                 'however', 'lead', 'system', 'order', 'plan', 'keep', 'face', 'group', 'play', 'stand', 'increase', 
                'early', 'course', 'change', 'help', 'line', 'possible', 'fact', 'down'] 
# first way 
# make variable to store word in the list 
lst_words = []
#initialize for loop 
for word in words:
#add each items uppercase  in the list with up    
    lst_words.append( word.upper())
#print result 
print(lst_words)
#############################################    
# second way 
#initialize for loop 
for word in words:
#print result   
    print( word.upper())
