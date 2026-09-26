tasks = []


def show_menu():
    print("\n--- To-Do List ---")
    print("1. Add Task")
    print("2. View Task")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")


def add_task():
    task = input("Enter Task : ")
    tasks.append({"task": task, "Done": False})
    print(f"Task '{task}'  added!")


def view_task():
    if not tasks:
        print("No task yet!")
        return
    print("\n Your Tasks: ")

    for index, task in enumerate(tasks, start=1):
        status = "☑" if task["Done"] else "❌"
        print(f"{index}. {task["task"]} [{status}]")


def mark_done():
    view_task()
    if not tasks:
        return
    try:
        index = int(input("Enter task number to mark done :3 ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["Done"] = True
            print("Marked as done!")
        else:
            print("Invalid number!")
    except ValueError:
        print("Please enter a valid number.")


def delete_task():
    view_task()
    if not tasks:
        return
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"Delete tasks: {removed['task']}")
        else:
            print("invalid number!")
    except ValueError:
        print("Please enter a valid number.")


while True:
    show_menu()
    choice = input("choice option between 1 to 5 : ")

    if choice == '1':
        add_task()
    elif choice == '2':
        view_task()
    elif choice == '3':
        mark_done()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("Goodbye :)\n")
        break
    else:
        print("Invalid choice. try again")
