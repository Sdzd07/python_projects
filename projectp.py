#program that calculate the average score of a student and interact
list_degrees = []
while True:
#get input from user     
    message = input("Enter score,(or type 'done', to exit) :").lower()
#if message not equal "done" do that   
    if message != "done":
#add score into the list         
        list_degrees.append(int(message))         
#sum all the scores into the list         
        sum_list_degrees = sum(list_degrees)
#calculate the average of th scorse        
        average = sum_list_degrees/len(list_degrees)
#if message equal "done" do that    
    else:
         if list_degrees != []:
#print the result and stop the program 
            print("_"*50) 
            print(f"The average of scorse is : {average}")
            break     
         else:
            break   

        
          
