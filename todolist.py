import datetime

tasks = []

def show_menu():
    print("\n📋 --- TO-DO LIST ---")
    print("1. ➕ Add Task")
    print("2. 📜 View Tasks")
    print("3. ✅ Mark Task as Done")
    print("4. ✏️  Update Task Name")
    print("5. ❌ Delete Task")
    print("6. 🚪 Exit")

def add_task():
    task_name = input("Enter task name: ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    tasks.append({"task": task_name, "status": "Pending", "created": timestamp})
    print("✅ Task added!")

def view_tasks():
    if not tasks:
        print("😴 No tasks found.")
    else:
        print("\n📌 Your Tasks:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. [{task['status']}] {task['task']} (Added on {task['created']})")

def mark_done():
    view_tasks()
    try:
        idx = int(input("Enter task number to mark as done: ")) - 1
        if 0 <= idx < len(tasks):
            tasks[idx]['status'] = 'Done'
            print("✅ Task marked as done.")
        else:
            print("❗ Invalid task number.")
    except ValueError:
        print("❗ Please enter a valid number.")

def update_task():
    view_tasks()
    try:
        idx = int(input("Enter task number to update: ")) - 1
        if 0 <= idx < len(tasks):
            new_name = input("Enter new task name: ")
            tasks[idx]['task'] = new_name
            print("✏️ Task updated.")
        else:
            print("❗ Invalid task number.")
    except ValueError:
        print("❗ Please enter a valid number.")

def delete_task():
    view_tasks()
    try:
        idx = int(input("Enter task number to delete: ")) - 1
        if 0 <= idx < len(tasks):
            tasks.pop(idx)
            print("🗑️ Task deleted.")
        else:
            print("❗ Invalid task number.")
    except ValueError:
        print("❗ Please enter a valid number.")

while True:
    show_menu()
    choice = input("Choose an option (1-6): ").strip()

    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        mark_done()
    elif choice == '4':
        update_task()
    elif choice == '5':
        delete_task()
    elif choice == '6':
        print("👋 bye! ")
        break
    else:
        print("❗ Invalid choice. Please select from 1 to 6.")
