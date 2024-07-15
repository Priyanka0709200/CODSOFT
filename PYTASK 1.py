# Define an empty list to store tasks
tasks = []

# Function to display the menu options
def display_menu():
    print("===== To-Do List App =====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task as Completed")
    print("6. Exit")
    print("==========================")

# Function to view tasks in the list
def view_tasks():
    if not tasks:
        print("No tasks in the list.")
    else:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task['task']} - {'Completed' if task['completed'] else 'Pending'}")

# Function to add a new task to the list
def add_task():
    task_name = input("Enter task name: ")
    task = {'task': task_name, 'completed': False}
    tasks.append(task)
    print(f"Task '{task_name}' added successfully.")

# Function to update an existing task in the list
def update_task():
    view_tasks()
    try:
        task_index = int(input("Enter task number to update: ")) - 1
        if 0 <= task_index < len(tasks):
            new_task_name = input("Enter new task name: ")
            tasks[task_index]['task'] = new_task_name
            print("Task updated successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Function to delete a task from the list
def delete_task():
    view_tasks()
    try:
        task_index = int(input("Enter task number to delete: ")) - 1
        if 0 <= task_index < len(tasks):
            del tasks[task_index]
            print("Task deleted successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Function to mark a task as completed
def mark_completed():
    view_tasks()
    try:
        task_index = int(input("Enter task number to mark as completed: ")) - 1
        if 0 <= task_index < len(tasks):
            tasks[task_index]['completed'] = True
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Main function to run the To-Do List app
def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            update_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            mark_completed()
        elif choice == '6':
            print("Thank you for using the To-Do List App.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()
