def task():
    tasks = []
    print("Welcome to the To-Do App!")
    
    total_tasks = int(input("How many tasks do you want to add => ")) #5  
    for i in range(total_tasks):
        task = input(f"Enter task {i+1}: ")  #enter task 3 =
        tasks.append(task)
        
    print(f"\nYour To-Do List: \n{tasks}")
    
    while True:
        operation = int(input("\nChoose an operation - 1: Add Task, 2: Update Task, 3: Delete, 4: Total Task, 5: Exit /Stop/= "))
        if operation == 1:
            add = input("Enter the task you want to add:")
            tasks.append(add)
            print(f"Task {add} has been successfully added...")
            
        elif operation == 2:
            updated_val = input("Enter the task name you want to update = ")
            if updated_val in tasks:
                up = input("Enter new task = ")
                ind = tasks.index(updated_val) #2
                tasks[ind] = up
                print(f"Updated task = {up}")
                
        elif operation == 3:
            del_val = input("Which task you want to delete = ")
            if del_val in tasks:
                ind = tasks.index(del_val)
                del tasks[ind]
                print(f"Task {del_val} has been deleted...")
                
        elif operation == 4:
            print(f"Total tasks is = {tasks}")
            
        elif operation == 5:
            print("Closing of the programm...")
            break
        
        else:
           print("Invalid Input") 
            
                
task()


print("Hello World")