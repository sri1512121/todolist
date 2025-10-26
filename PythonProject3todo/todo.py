import json

# File to store tasks
FILENAME = "tasks.json"

# Load tasks from file
def load_tasks():
    try:
        with open(FILENAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save tasks to file
def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        json.dump(tasks, file, indent=4)

# Add a new task
def add_task(tasks):
    task = input("Enter your new task: ")
    tasks.append({"task": task, "completed": False})
    print(f"Task '{task}' added!")

# View all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    for i, task in enumerate(tasks, 1):
        status = "✔️" if task["completed"] else "❌"
        print(f"{i}. {task['task']} [{status}]")

# Update a task
def update_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter task number to mark as completed: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["completed"] = True
            print(f"Task '{tasks[index]['task']}' marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Delete a task
def delete_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"Task '{removed['task']}' deleted!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main program loop
def main():
    tasks = load_tasks()
    while True:
        print("\n--- TO-DO LIST MENU ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
            save_tasks(tasks)
        elif choice == "3":
            update_task(tasks)
            save_tasks(tasks)
        elif choice == "4":
            delete_task(tasks)
            save_tasks(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
