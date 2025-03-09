# program always asks user for input:
# 1- when user enters line ,print it
# 2- when user enters done, program stops and print done!
# 3- when user start line with # or preesse Enter key, it ignores the line 

#  greate while for always ask user to enter input 
while True:
# greate variable for get input from user
  message = input("Enter input:").strip() 
 #conditionl if user enters # or preese enter key, program ingorse the line  
  if  len(message)== 0  or message[0] == "#":
    continue
  #if user enters done, program stops and print done
  elif message.lower() == "done":
    print("Done!")
    break
  #if the tow previouse conditons are not met then print message 
  else:
    print(message)       