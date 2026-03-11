'''
The Scenario:
You have a dictionary of users and their roles. 
You also have a list of "Fired Employees" 
who need to be removed from the system immediately.

The Task:

Loop through the fired_employees list.

Check if that employee exists in your system_users dictionary.

Delete them if they exist.

'''
system_users = {"mohsan": "admin", "john": "user", "jane": "user", "bob": "guest"}
fired_employees = ["john", "bob", "malicious_user"]
try:
    for employee in fired_employees:
        if employee in system_users:
            print(f'{employee} is Fired  Now')
            system_users.pop(employee)

    print(f"Remaining Users: {system_users}")
except NameError:
    print('Error Occured')