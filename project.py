#this program work by this ask you for enter a word and will reversed it 
#get input from user 
word = input("Enter a word: ")
#change the string to list 
list_word = word.split()
#for reversed the word use sort with reversed option 
reversed_word = list_word.sort(reverse = True)                              
print(reversed_word)