#Make a list of tuples with the first element as the word and the second element as the length of the word. . 
words = ["Hello", "from", "Codezilla", "Python", "Course"] 
word_lenght = [ (word,len(word)) for word in words]
print(word_lenght)