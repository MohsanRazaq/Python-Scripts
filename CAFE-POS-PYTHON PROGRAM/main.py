'''
The Challenge Requirements
The Setup: Start with inventory 

The Infinite Loop:
Use while True: so the cafe stays "open" for multiple customers.

Step A: Item Selection
Ask the user: "What would you like? (Type 'status' to see menu, or 'exit' to close): ".

If status: Print the current inventory.

If exit: Break the loop and save to a file.

If the item is not in the dictionary: Print "We don't sell that!" and use continue to restart the loop.

Step B: Quantity & Validation (The Hard Part)
If the item exists, ask: "How many? ".

CRITICAL: Use a try/except block. If the user types "two" instead of 2, the program must not crash. It should say "Invalid number!" and go back to the start.

Step C: Inventory Check

If quantity > inventory[item]: Print "Not enough in stock! We only have {count} left."

Otherwise: Subtract the amount and print "Order successful!"

The File Save:
When the loop breaks (on 'exit'), write a clean summary to final_report.txt.

'''
inventory={
"sprite":55,
"Coke":10,
"pepsi":50,
"Juice":5
}
print("--------------------Welcome to Cafe-------")
print("-------------------What would you like:--------------")
while True:
    print("nType 'menu' to see Menu, or 'q' to close): ")
    choice=input("Enter Your choice:").lower()
    try:
        if choice =='q':
            print("Thanks For Having Time with Us " )
            with open("final_report",'w') as f:
                f.write(f"Hello this is final report for our  cafe\n")
                f.write(f"Updated inventory:\n{" ,".join(inventory)}")
            break
        elif  choice=='menu'.lower():
            for item,counts in inventory.items():
                print(item)
            option=input('Select Your Desired Item: ')
            if option not in inventory:
                print(f"We don't sell {option}")
                continue    
            try:
                quantity=int(input('How Much you need.Enter  quantity: '))
                if quantity >inventory[option]:
                    print(f"Not enough in stock! We only have {inventory[option]} left")
                else:
                    print("Your Order details are below:")
                    print(f"You Have ordered {option}\nQuantity: {quantity}")
                    inventory[option]-=quantity
            except ValueError:
                print("Invalid Number")
            
        else:
            print('Invalid Choice.Try Again')

    except ValueError:
        print(f'Invalid-->{ValueError}')