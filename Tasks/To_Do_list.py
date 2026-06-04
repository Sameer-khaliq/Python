import os

class ToDoManager:
    def __init__(self, filename="todo.txt"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        """File se tasks load karne ka logic (File I/O with Exception Handling)"""
        try:
            if os.path.exists(self.filename):
                with open(self.filename, "r") as file:
                    # Strip lines removes spaces and newlines
                    self.tasks = [line.strip() for line in file.readlines()]
            else:
                self.tasks = []
        except IOError as e:
            print(f"Error loading file: {e}")
            self.tasks = []

    def save_tasks(self):
        """Tasks ko text file mein save karne ka logic"""
        try:
            with open(self.filename, "w") as file:
                for task in self.tasks:
                    file.write(f"{task}\n")
        except IOError as e:
            print(f"Error saving data to file: {e}")

    def add_task(self, task):
        if not task:
            print("Task empty nahi ho sakta!")
            return
        self.tasks.append(task)
        self.save_tasks()
        print(f"Task successfully added: '{task}'")

    def list_tasks(self):
        if not self.tasks:
            print("\n--- No tasks found! Relax karo. ---")
            return
        print("\n=== YOUR TO-DO LIST ===")
        for index, task in enumerate(self.tasks, start=1):
            print(f"{index}. {task}")
        print("=======================")

    def remove_task(self, index):
        try:
            # 1-based index ko 0-based index balance karne ke liye
            removed = self.tasks.pop(index - 1)
            self.save_tasks()
            print(f"Removed task: '{removed}'")
        except IndexError:
            print("Invalid task number! List check karo.")

def main():
    manager = ToDoManager()
    
    while True:
        print("\n1. Add Task | 2. View Tasks | 3. Delete Task | 4. Exit")
        choice = input("Option select karein (1-4): ").strip()
        
        if choice == "1":
            task = input("Task text likhein: ").strip()
            manager.add_task(task)
        elif choice == "2":
            manager.list_tasks()
        elif choice == "3":
            manager.list_tasks()
            if manager.tasks:
                try:
                    num = int(input("Kon sa task delete karna hai? (Number): "))
                    manager.remove_task(num)
                except ValueError:
                    print("Invalid input! Number input karein.")
        elif choice == "4":
            print("Goodbye! Progress saved.")
            break
        else:
            print("Invalid choice, choose between 1 to 4.")

if __name__ == "__main__":
    main()