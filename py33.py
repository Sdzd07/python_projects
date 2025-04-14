#Edit words list to gain the following outputs. 
words = [["Hello", "from", "Codezilla"],  ["Python", "Course", "is", "awesome"],  ["I", "enjoy", "learning", "Python", "with", "Codezilla"]] 
#convert each inner list to astring and join them with space and add on the list 
modify_list = [" ".join(sentence) for sentence in words ]
#make another list and replace space to dashes and convert all words on th list to uppercase
uppercase_list = [ sentence.replace(" ","_").upper() for sentence in modify_list]
# print result
print(modify_list)
print(uppercase_list)
