tasks = []  

def add_task(task):
    tasks.append(task)
    print(f"Your Task '{task}' is added to your to do list!")

def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print(f"Your Task '{task}'is removed from your to do list!")
    else:
        print(f"Sorry Task '{task}' not found!")

def show_tasks():
    if tasks:
        print("Your To-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("Your to-do list is empty.")


while True:
    print("\n1. Add Task")
    print("2. Remove Task")
    print("3. Show Tasks")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        task = input("Enter the task you want to add to you to-do list: ")
        add_task(task)
    elif choice == '2':
        task = input("Enter the task to remove from your to-do list: ")
        remove_task(task)
    elif choice == '3':
        show_tasks()
    elif choice == '4':
        print("Exiting the to-do list. Thank you!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
