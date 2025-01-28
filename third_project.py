#this program for guss the word if start with a vowel
#get input from user 
word = input("Enter a word: ").lower()
#add vowel on variable
vowel = "aeuo"
guss = input(f"Dose the {word} start with a vowel? ")
#do comparison between the input and the vowel and output the result
if word[0] in vowel and guss.lower() == "yes":
    result = f"bravooo\n{word} start with vowel"
elif word[0] not in vowel and guss.lower() == "no":
    result =  f"bravooo\n{word} dose not start with vowel"  
else:
    result = "Let's try again"  
print("_"*50)
print(result)      
