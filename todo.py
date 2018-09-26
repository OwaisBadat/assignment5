class task:
    def __init__(self,title,priority):
        self.title = title
        self.priority = priority


    def __repr__(self):
        return "Task = {0} and priority = {1}".format(self.title,self.priority)

task_list = []



def display_tasks(tasks):
    for i in tasks:
        print(i)

while True:
    user_input = input("Add task enter 'A', remove the tasks enter 'R', view task list 'V', if you woud like to exit press 'Q': ").lower()

    if user_input == "q":
        break

    elif user_input == "a":
        task_title = input("Enter your task: ")
        priority = input("Tpye priority High, Low, Medium: ").upper()
        task_list.append(task(task_title,priority))

    elif user_input == "v":
        display_tasks(task_list)

    elif user_input == "r":
        del task_list
        task_list = []
        print("List deleted:")

    else:
        print("Input not valid, please try again.")
