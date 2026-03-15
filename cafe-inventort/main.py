''''
Scenario:
"The Neighborhood Cafe Inventory"
You ve been hired by a local cafe to manage their daily inventory. They need a way to track what’s in stock, handle sales, and save the final report to a text file so the owner can review it the next morning.

The Challenge
Write a Python script that performs the following tasks:

Initialize Inventory:
Create a dictionary where the keys are item names (e.g., "Latte", "Croissant", "Espresso") and the values are their current stock counts (integers).

Process Sales:
Create a list of "Sale" tuples or dictionaries representing items sold during a shift (e.g., [("Latte", 2), ("Espresso", 1)]).

Update Stock:
Loop through the sales list and subtract the sold amounts from your inventory dictionary.

Bonus: Add a check to see if you have enough stock before "selling" it. If not, print a warning.

Calculate Low Stock:
Identify any items that have fewer than 5 units left and store them in a new list called restock_alerts.

File Export:
Write the final inventory state and the restock_alerts into a file named end_of_day_report.txt
'''
# Starting Inventory
inventory = {
    "Latte":       20,
    "Croissant":   0,
    "Espresso":    15,
    "Muffin":      3
}
restock_alerts=[]
# Sales that occurred
daily_sales = [("Latte", 3), ("Croissant", 5), ("Muffin", 1), ("Latte", 2)]
for item,amount in daily_sales:
    if inventory[item]>=amount:
        inventory[item]-=amount
    else:
        print(f"Warning---> Your Stock IS low  for {item}")

for item,count in inventory.items():
    if inventory[item] <5:
        restock_alerts.append(item)
with open("end_of_day_report.txt",'w') as f:
    f.write(f"Here is End of the Day report\n")
    f.write(f"Final Inventort: {" ".join(inventory)}\n")
    f.write(f"Restock_alerts: \n{"\n".join(restock_alerts)}")