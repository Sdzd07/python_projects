#program
contacts = [   
            ("Mohamed Gouda", "+1-555-555-5555","mohamedgouda@example.com"),
            ("Amira Abdelrahman", "+1-555-555-5556","amiraabdelrahman@example.com"),
            ("Abdullah Othman", "+1-555-555-5557","abdullahothman@example.com"),
            ("Ahmed Saeed", "+1-555-555-5558","ahmedsaeed@example.com"),
            ("Saleh Abdelhamid", "+1-555-555-5559","salehabdelhamid@example.com"),
            ("Fatima Ali", "+1-555-555-5560", "fatimaali@example.com"),
            ("Omar Hasan", "+1-555-555-5561", "omarhasan@example.com"),
            ("Aisha Ahmed", "+1-555-555-5562","aishaahmed@example.com"),
            ("Karim hassen", "+1-555-555-5563","karimhassan@example.com")
            ]

while True:
   print("Welcome to the phonebook application!\n1. Add a contact\n2. Update a contact\n3. Search for a contact\n4. Quit")
   choice = int(input("Enter your choice: "))
   if choice == 1:
      name = input("Enter name: ")
      phone_number = input("Enter phone number: ")
      address_email = input("Enter address email: ")
      contacts.append((name,phone_number,address_email))
      print(contacts)
      print("Contact added successfully\n-----------------------------------")
   elif choice == 2:
         update_name= input("Enter name of the contact you want to update: ")
         for i in range(len(contacts)):
            if update_name.lower() == contacts[i][0].lower() :
               update_number = input("Enter new phone number: ")
               update_address = input("Enter new email: ")
               contacts[i] = (update_name,update_number,update_address)
               print("Contact updated successfully.\n--------------------------------")
               break
         else: 
               print("Contact not found.")   
   elif choice == 3:
         search = input("Enter name of the contact you want to search: ")
         for i in range(len(contacts)):
            if  contacts[i][0].lower() == search.lower() :
               name,phone_number,address_email == contacts[i] 
               print(f"Name: {name}\nPhone number: {phone_number}\naddress email: {address_email}\n___________________________________")
               break
         else:
             print("Contact not found.")   
   elif choice == 4:
        break
   else: 
       print("invalid choice\n-----------------------")

