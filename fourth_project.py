#this program calculate the number of charcters and spaces in the text
# and calculate the characters without space means give tow results so lest start :
# get input from user(by the way we can ask user or we can put list befor)
text = input("writ text please: ").strip()
new_text = len(text)
#now the steps to calculate the characters without spaces in the text 
#now the problem is how we can remove the space in the text 
#solution is change the input (text) to the list by use split method   
text_lst = text.split()
#second change the text_lst to an one string by use join method 
text_without_space = "".join(text_lst) 
#output the results for user 
print("_"*50)
print(f"Numbers of characters with space is: {new_text}")
print(f"Number of characters without sapce is: {len(text_without_space)}")
