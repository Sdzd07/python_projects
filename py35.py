#Flat the following nested list. . 
nested_list = [["Hello", "from", "Codezilla"],  ["Python", "Course", "is", "awesome"],  
               ["I", "enjoy", "learning", "Python", "with", "Codezilla"]
              ] 
words_list = [ word for sentence in nested_list for word in sentence ]
print(words_list)