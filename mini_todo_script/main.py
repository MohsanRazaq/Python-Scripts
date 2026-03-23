import os
os.makedirs("mini_todo_script", exist_ok=True)
accounts_file = "mini_todo_script/accounts.txt"

## ---------------- Account --------------------

def create_account():
    name = input('Enter Name: ').strip()
    while True:
        Pass = input('Enter your Secret 4 digit Pin: ').strip()
        if Pass.isdigit() and len(Pass) == 4:
            break
        else:
            print('Error: PIN must be exactly 4 digits\n')
            
    if not os.path.exists(accounts_file):
        open(accounts_file, 'w').close()
            
    with open(accounts_file, 'r') as f:
        for line in f:
            if "|" in line:
                user_name, _ = line.strip().split('|')
                if user_name == name:
                    print('User Name Already taken')
                    return 
                    
    with open(accounts_file, 'a') as f:
        f.write(f'{name}|{Pass}\n')            
    print(f"Account Created\nUsername: {name}\nPin: {Pass}")    
            
def login():
    if not os.path.exists(accounts_file):
        print('no Account Found')
        return None
    name = input('Enter your name: ').strip()
    Pass = input('Enter your pin: ').strip()
    with open(accounts_file, 'r') as f:
        for line in f:
            if "|" in line:
                user_name, user_pass = line.strip().split('|')
                if name == user_name and Pass == user_pass:
                    print(" Login Successful")
                    return name
    print("Invalid Username or PIN")
    return None

## ---------------- Tasks Section --------------------

def get_task_file(username):
    return f"mini_todo_script/{username}_tasks.txt"

def add_task(username):
    filename = get_task_file(username)
    task_name = input('Enter name of the Task: ').strip()
    is_it_urgent = input(f'Is {task_name} urgent? (yes/no): ').lower().strip()
    
    with open(filename, 'a') as f:
        status = 'Urgent' if is_it_urgent == 'yes' else 'Normal'
        f.write(f'{task_name}|{status}\n')
        
    print(f' {task_name} added to list.') 

def view_tasks(username):
    file = get_task_file(username)
    if not os.path.exists(file):
        print(" No tasks found.")
        return []
    
    with open(file, 'r') as f:
        tasks = f.readlines()
        
    if not tasks:
        print("Your list is empty.")
        return []

    for i, line in enumerate(tasks):
        if "|" in line:
            task, status = line.strip().split('|')
            print(f'{i}. {task} [{status}]')
    return tasks

def delete_task(username):
    tasks = view_tasks(username)
    if not tasks:
        return 
        
    try:
        idx = int(input('Enter Task index to delete: '))
        if 0 <= idx < len(tasks):
            removed = tasks.pop(idx)
            with open(get_task_file(username), 'w') as f:
                f.writelines(tasks)
            print(f' Deleted: {removed.split("|")[0]}') ## we use 2 things here one id delimeter to remove extra things like status from our   deleted task and 2 is 0 index..we telling python to get only 1 task
        else:
            print(" Invalid Index.")
    except ValueError:
        print(' Please enter a valid number.')

## ---------------- Update Tasks  --------------------

def update_task(username):
    tasks = view_tasks(username)
    if not tasks:
        return 
        
    try:
        idx = int(input('Enter Task index to update status: '))
        
        # Validation
        if 0 <= idx < len(tasks):
            # We use split("|", 1) to be safe if the task has a pipe in it
            current_task_name = tasks[idx].split("|")[0]

            new_status_input = input(f"Update '{current_task_name}' to Urgent? (yes/no): ").lower().strip()
            new_status = "Urgent" if new_status_input == 'yes' else "Normal"
            tasks[idx] = f"{current_task_name}|{new_status}\n"
        
            with open(get_task_file(username), 'w') as f:
                f.writelines(tasks)
                
            print(f"Task '{current_task_name}' updated to {new_status}.")
        else:
            print(" Invalid Index.")
            
    except ValueError:
        print(' Please enter a valid number.')

def menu(name):
    while True:
        print(f'\n--- {name.upper()}\'S MANAGER ---')
        print('1-Add Task\n2-View Tasks\n3-Delete Task\n4-Update task\n5-Logout')
        choice = input('Enter choice: ')
        
        if choice == '1':
            add_task(name)
        elif choice == '2':
            view_tasks(name)
        elif choice == '3':
            delete_task(name)
        elif choice == '4':
            update_task(name)
        elif choice == '5':
            break
        else:
            print('Invalid choice.')

def main():
    while True: 
        print('\n--- MAIN MENU ---')
        print('1) Create Account\n2) Login\n3) Exit') 
        choice = input('Select: ') 
        
        if choice == '1':
            create_account()
        elif choice == '2':
            user = login()
            if user:
                menu(user)
        elif choice == '3':
            print('Goodbye!')
            break
        else:
            print('Select 1, 2, or 3.')

if __name__ == "__main__":
    main()