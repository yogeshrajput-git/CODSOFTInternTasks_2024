import os

# Define the file where tasks will be stored
TASKS_FILE = "tasks.txt"

def load_tasks():
    """Load tasks from the file."""
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as file:
        tasks = file.readlines()
    return [task.strip() for task in tasks]

def save_tasks(tasks):
    """Save tasks to the file."""
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def display_tasks(tasks):
    """Display the list of tasks."""
    if not tasks:
        print("No tasks found.")
    else:
        print("\nTo-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def add_task(tasks):
    """Add a new task to the list."""
    task = input("Enter the task description: ")
    tasks.append(task)
    print("Task added.")

def update_task(tasks):
    """Update an existing task."""
    display_tasks(tasks)
    try:
        index = int(input("Enter the number of the task to update: ")) - 1
        if 0 <= index < len(tasks):
            new_description = input("Enter the new task description: ")
            tasks[index] = new_description
            print("Task updated.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def delete_task(tasks):
    """Delete a task from the list."""
    display_tasks(tasks)
    try:
        index = int(input("Enter the number of the task to delete: ")) - 1
        if 0 <= index < len(tasks):
            tasks.pop(index)
            print("Task deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    """Main function to manage the to-do list application."""
    tasks = load_tasks()
    
    while True:
        print("\nTo-Do List Menu:")
        print("1. Display tasks")
        print("2. Add task")
        print("3. Update task")
        print("4. Delete task")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
