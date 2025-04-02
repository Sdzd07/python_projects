#Make a program that print contacts info

contacts = [('Mohamed Gouda', '+1-555-555-5555','mohamedgouda@example.com'), 
            ('Amira Abdelrahman', '+1-555-555-5556', 'amiraabdelrahman@example.com'), 
            ('Abdullah Othman','+1-555-555-5557', 'abdullahothman@example.com'),
            ('AhmedSaeed', '+1-555-555-5558', 'ahmedsaeed@example.com'),
            ('SalehAbdelhamid', '+1-555-555-5559', 'salehabdelhamid@example.com'),
            ('Fatima Ali', '+1-555-555-5560', 'fatimaali@example.com'),
            ('Omar Hasan', '+1-555-555-5561', 'omarhasan@example.com'),
            ('Aisha Ahmed', '+1-555-555-5562', 'aishaahmed@example.com'),
            ('Karim Hassan', '+1-555-555-5563', 'karimhassan@example.com')
            ]
# initialize for loop and umpaking tupl and makes varaibles for for each value 
print("Contact Information\n---------------------------------------")
for  name, phone_number, address_email, in contacts:
    print(f"Name :{name}\nPhone number : {phone_number}\nAddress email: {address_email}")  
    print("_"*40) 
#########################
#second way
print("Contact Information\n----------------------------------------")
for  contact in contacts:
    print(f"Name :{contact[0]}\nPhone number : {contact[1]}\nAddress email: {contact[2]}")  
    print("_"*40) 