#Find the average word length in the following sentence.  
sentence = """Python is a widely used high-level  general-purpose interpreted dynamic programming language Its design philosophy emphasizes code readability and its syntax 
              allows programmers to express concepts in fewer lines of code  than possible in many other languages The language provides constructs intended to enable clear 
              programs on both a small and large scale 
           """
# step one make variable for strod the total words lenght
len_words = 0
#initialize for loop for sentences 
for word in sentence:
#calculat the toatal words lenght     
    len_words+=len(word)
#convert sentence to list 
spl_sentence = len(sentence.split())
#calculat the average word lenght 
len_average = (len_words)/(spl_sentence)
#print result 
print(f"The total words lenght is: {len_words} letters") 
print(f"The average word lenght is: {int(len_average)} letters")
