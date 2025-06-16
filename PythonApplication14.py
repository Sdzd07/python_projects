# dictionary with the words and definitions#Make your English study helper program that help you like the following.

words = {
"Absence":"The lack or unavailability of something or someone.",
"Approval":"Having a positive opinion of something orsomeone.",
"Answer":"The response or receipt to a phone call,question, or letter.",
"Attention":"Noticing or recognizing something ofb interest.",
"Amount":"A mass or a collection of something",
"Borrow":"To take something with the intention of returning it after a period of time.",
"Baffle":"An event or thing that is a mystery and confuses.",
"Ban":"An act prohibited by social pressure or law.",
"Banish":"Expel from the situation, often done officially.",
"Banter":"Conversation that is teasing and playful.",
"Characteristic":"referring to features that are typical to the person, place, or thing.",
"Cars":"Four-wheeled vehicles used for traveling.",
"Care":"extra responsibility and attention.",
"Chip":"a small and thin piece of a larger item.",
"Cease":"to eventually stop existing.",
"Dialogue":"A conversation between two or more people.",
"Decisive":"a person who can make decisions promptly.",
}
import random
while True:
    print("1. Review random word\n2. Test yourself\n3. Eixt")
    choice = input("Enter your choice:")
    if choice=="1":
        random_word = random.choice(list((words.keys())))
        print(f"Word: {random_word}")
        print(f"Definition: {words[random_word]}")
    elif choice=="2":
         random_word = random.choice(list((words.keys())))
         print(f"Definition: {words[random_word]}")
         counter = 1
         found = True
         while found!=False:
            word = input("Enter the word: ").lower().title()
            if word not in words: 
                if counter!=3:
                    print("Worng answer you have one more attempt")
                    counter+=1
                else: 
                    print("Worng answer you have no more attempt")          
                    print(f"The corecte answer is: {random_word}")
                    found = False
            else:
                print("Corecte answer")    
                break          
    elif choice=="3":
        print("Have a nice day!")
        break
    else:
        print("Invalid option")
