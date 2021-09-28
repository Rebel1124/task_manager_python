#Import datetime library
import datetime

#Next we create a set of functions which we will be calling in our program
#The functions help us modulize our program and also it makes it easy for us to pick up and fix bugs

#This function takes in a string (dat string) and converts to a date
def set_date(in_date):
    in_date = check_date(in_date)
    s_date = in_date.split()
    s_date[1] = months.index(s_date[1])
    dt_date = datetime.date(int(s_date[2]), int(s_date[1]), int(s_date[0]))
    return dt_date

#The below function writes out the tasks to the tasks.txt file
def write_task():
    #Here I count the number of tasks
    count = len(task_assign)

    #Here we open the tasks.txt file and add the new task to the file
    tasks_file = open("tasks.txt", "w")

    for i in range(0, count):
        lines = task_assign[i]+", "+task_title[i]+", "+task_description[i]+", "+task_date[i]+", "+task_due[i]+", "+task_completed[i]+"\n"
        tasks_file.write(lines)
    
    #We then close the file
    tasks_file.close()


#The below function writes out the users to the users.txt file
def write_user():
    #Here I count the number of registered users, which I will then write to the user.txt file
    count = len(login_names)

    #Open the user file and write the names and passowrd of users from the login_names and login_passwords lists
    user_file = open("user.txt", "w")

    for i in range(0, count):
        lines = login_names[i]+", "+login_passwords[i]+"\n"
        user_file.write(lines)
    
    #Close the user file
    user_file.close()


#Check if date is in correct format - this function takes in a sting (date string as input)
def check_date(input_date):
    #Below are the applicable months
    months=['January', 'February', 'March', 'April', 'May', 'June', 'July',
            'Augst', 'September', 'October', 'November', 'December']

    #Here we plit the input date (i.e. the date to check into a list - day month year)                
    d_date = input_date.split()
    
    #Count the lenngth of the list
    count = len(d_date)

    #Next we perform check to ensure that the date the user entered isin the correct format

    #First check that the lenght of the list is 3, if not ask user to enter the date in teh correct format
    while count != 3:
        input_date = input("a New due date in correct format(day Month Year): ")
        d_date = input_date.split()
        count = len(d_date)

    #Here we check that the days input is an integer, if not ask user to re-enter date
    while True:
        try:
            d_date[0] = int(d_date[0])
            break
        except ValueError:
            input_date = input("b New due date in correct format(day Month Year): ")
            d_date = input_date.split()
            count = len(d_date)

    #Next we check that the days input is the correct day range, if not ask user to re-enter date
    while d_date[0] not in range(1,32):
        input_date = input("c New due date in correct format(day Month Year): ")
        d_date = input_date.split()
                        
        while True:
            try:
                d_date[0] = int(d_date[0])
                break
            except ValueError:
                input_date = input("d New due date in correct format(day Month Year): ")
                d_date = input_date.split()
                count = len(d_date)

    #Nex we check that the months input is the months list defined earlier, if not ask user to re-enter date
    while d_date[1] not in months:
            print(d_date)
            input_date = input("e New due date in correct format(day Month Year): ")
            d_date = input_date.split()
            count = len(d_date)
    
    #Here we check that the year input is an integer, if not ask user to re-enter date
    while True:
        try:
            d_date[2] = int(d_date[2])
            break
        except ValueError:
            input_date = input("f New due date in correct format(day Month Year): ")
            d_date = input_date.split()
            count = len(d_date)

    #Here we check that the year input is the correct year range, if not ask user to re-enter date
    while d_date[2] not in range(1000,9999):
        input_date = input("gNew due date in correct format(day Month Year): ")
        d_date = input_date.split()                       
                        
        while True:
            try:
                d_date[2] = int(d_date[2])
                break
            except ValueError:
                input_date = input("h New due date in correct format(day Month Year): ")
                d_date = input_date.split()
                count = len(d_date)
    
    return input_date


#Below is a function to display the options for the user to select
def options():
    if (username == "admin"):
        print("\nPlease select one of the following options: ")
        print("r-register user")
        print("a-add task")
        print("va-view all tasks")
        print("vm-view my tasks")
        print("gr-generate reports")
        print("dr-display report")
        print("ds - statistics")
        print("e - exit")
    else:
        print("\nPlease select one of the following options: ")
        print("r - register user")
        print("a - add task")
        print("va - view all tasks")
        print("vm - view my tasks")
        print("e - exit")

#Create reg_user function
def reg_user():

    usrname = input("\nUsername for new user: ").lower()    #to register a user enter a username for the user
    
    while usrname in login_names:
        usrname = input("Username already regitered, please enter new username: ").lower()

    pswd = input("Password for new user: ")                 #ask admin user to enter a password for the user
    confirm_pswd = input("Re-enter new password: ")         #ask admin user to re-enter password for the new user

    #The below while loop will check if the re-entered password and the initial password eneters matches
    #If they do not match, the continue to ask the admin user to update the re-entered password until 
    #it matches the initial password entered
    while pswd != confirm_pswd:
        confirm_pswd = input("Re-enter new password: ")

    #We then append the new user and password to the respective login_names and login_passwords lists
    login_names.append(usrname)
    login_passwords.append(pswd)

    write_user()

#Create add_task function
def add_task():

    #Ask user for task inputs
    assign_input = input("Who is the task assigned to: ").lower()
    title_input = input("Task title: ")
    description_input = input("Task description: ")
    date_input = input("date task was assigned (day Month Year): ")
    date_input = check_date(date_input)
    date_set = set_date(date_input)
    due_input = input("Task due date (day Month Year): ")
    due_input = check_date(due_input)
    due_set = set_date(due_input)
    completed_input = "No"

    #Here we assign the task inputs to the appropriate task_list
    task_assign.append(assign_input)
    task_title.append(title_input)
    task_description.append(description_input)
    task_date.append(date_input)
    task_due.append(due_input)
    task_completed.append(completed_input)
    task_set_date.append(date_set)
    task_due_date.append(due_set)

    #Check if the task is overdue or if we got time
    if (date_set > due_set):
        task_overdue.append("Overdue")
    else:
        task_overdue.append("Got Time")

    #call function to write out tasks to task.txt file
    write_task()


#Create view_all function
def view_all():
    #We count the number of tasks in our task_lists
    count = len(task_assign)

    #For each task, we print the attributes/characteristics of each task
    for j in range(0,count):
        print("\nTask "+str(j+1)+":")
        print("Title: \t\t"+task_title[j])
        print("Description: \t"+task_description[j])
        print("Assigned: \t"+task_assign[j])
        print("Entry Date: \t"+task_date[j])
        print("Due Date: \t"+task_due[j])
        print("Completed: \t"+task_completed[j])
        print("Progress: \t"+task_overdue[j])


#Create function to view and update user specific tasks     
def view_mine():
    #We count the number of tasks
    count = len(task_assign)
    #Here we set a count for the numer of tasks assigned to the user that is logged on, initially this is set to zero
    user_count = 0
    task_index = [-1]

    #For each task, we check if it has been assigned to the user thats logged on and
    #if it is, we then print out the characteristics of the respective task
    for j in range(0,count):
        if(task_assign[j] == username):
            print("\nTask "+str(j+1)+":")
            print("Title: \t\t"+task_title[j])
            print("Description: \t"+task_description[j])
            print("Assigned: \t"+task_assign[j])
            print("Entry Date: \t"+task_date[j])
            print("Due Date: \t"+task_due[j])
            print("Completed: \t"+task_completed[j])
            print("Progess: \t"+task_overdue[j])
            user_count += 1
            task_index.append((j+1))

    #Here we ask the user for which task of theirs they want to modify or enter -1 to return to main menu
    task_number = input("Select task to modify (enter task number) or -1 to return to main menu: ")

    #Check if task number is an integer
    while True:
        try:
            task_number = int(task_number)
            break
        except ValueError:
            task_number = input("Select task to modify (enter task number) or -1 to return to main menu: ")
    
    #Checks if task number is a task that belongs to the user that is logged on
    while task_number not in task_index:
        task_number = input("Select task to modify (enter task number) or -1 to return to main menu: ")
        while True:
            try:
                task_number = int(task_number)
                break
            except ValueError:
                task_number = input("Select task to modify (enter task number) or -1 to return to main menu: ")

    #If the user chooses a task to modify, we ask them what they want to modify and update the database accordingly     
    while task_number != -1 and task_number in task_index:

        for j in task_index[1:]:
                print("\nTask "+str(j)+":")
                print("Title: \t\t"+task_title[j-1])
                print("Description: \t"+task_description[j-1])
                print("Assigned: \t"+task_assign[j-1])
                print("Entry Date: \t"+task_date[j-1])
                print("Due Date: \t"+task_due[j-1])
                print("Completed: \t"+task_completed[j-1])
                print("Progess: \t"+task_overdue[j-1])

        print("\nPlease select from below options: ")
        print("complete-mark task as complete")
        print("edit-edit task")
        print("-1-go back to main menu")
        user_input = input("Please select complete, edit or -1: ")
        options = ['complete', 'edit', "-1"]

        #Checks that the user entered the correct option
        while user_input not in options:
            user_input = input("please select complete, edit or -1: ")

        #If the user updates the complete field then change field for this user and task to yes
        if (user_input == "complete"):
            task_completed[(task_number - 1)] = "Yes"

            #Update task text file
            write_task()

        #If user chooses edit check that task has not been marked as complete if it is, then alert user
        elif (user_input == "edit"):
            if(task_completed[(task_number - 1)] == "Yes"):
                print("Task {} has already been complted.".format(task_number))
            else:

                #Here we find out if the assigned user the same
                temp = input("Is the assigned user the same? (Yes or No): ").lower()

                #make sure correct choice has been entered     
                while temp not in ["yes", "no"]:
                    temp = input("Has the task been re-assigned? (Yes or No): ")
                
                #If task has been re-assigned then update user
                if(temp == "Yes"):
                    task_assign[(task_number - 1)] = input("New user: ")
                    #Write out to user text file
                    write_task()
            
                #Next we check with the user if the due date has changed
                temp = input("Has the due date changed? (Yes or No): ").lower()

                #make sure correct choice has been entered 
                while temp not in ["yes", "no"]:
                    temp = input("Has the due date changed? (Yes or No): ")

                #If the due date has changed ask user for new due date
                if(temp == "yes"):
                    deadline_date = input("New due date (day Month Year): ")
                    
                    #Check that the date entered is in te correct format
                    deadline_date = check_date(deadline_date)
                    
                    #Update due date for the respective task
                    task_due[(task_number - 1)] = deadline_date

                    #Check if the task is overdue or not
                    orig_set_date = set_date(task_date[(task_number -1)])
                    due_set_date = set_date(task_due[(task_number -1)])

                    if (orig_set_date > due_set_date):
                        task_overdue[(task_number - 1)] = "Overdue"
                    else:
                        task_overdue[(task_number - 1)] = "Got Time"

                    #Print out updated tasks to tasks file
                    write_task()
        
        #If the user enters -1 then we go back to the main menu
        elif (user_input == '-1'):
            break

    #If there are no tasks assigned to the user thats logged on, we display a message
    #saying that the user has no tasks assigned to them
    if (user_count == 0):
            print("There are no tasks assigned to this user!")

#Below functions displays task and user stats
def stats():
    #First we count the number of users and tasks
    num_users = len(login_names)
    num_tasks = len(task_assign)

    #Here we print the number of user and tasks
    print("There are {} users and {} tasks.".format(num_users, num_tasks))


#The function below generates the user_overview.txt and task_overview.txt files
def generate_report():

    #First find out the number of registered users and the number sof tasks
    total_tasks = len(task_assign)
    total_users = len(login_names)

    #caluclate how many tasks have been completed and how many have not
    comp=0
    for i in task_completed:
        if (i == "Yes"):
            comp+=1
    not_comp = total_tasks - comp

    #Calulate how many tasks are overdue
    overdue=0
    for j in range(0,total_tasks):
        if (task_overdue[j] == "Overdue" and task_completed[j] == "No"):
            overdue+=1
    #not_overdue = total_tasks - overdue 

    #Calculate the percentage of incomplete an overdue tasks
    percentage_tasks_incomplete = round(((not_comp/total_tasks)*100),2)
    percentage_tasks_overdue = round(((overdue/total_tasks)*100),2)


    #Here we open the tasks_overview.txt file and print out the results
    task_overview_file = open("task_overview.txt", "w")

    line0 = "\nTask Overview Report"
    line1 = "\nThe total number of tasks being tracked is: {}.".format(total_tasks)
    line2 = "\nThe total number of completed tasks is: {}.".format(comp)
    line3 = "\nThere total number of incomplete tasks is: {}.".format(not_comp)
    line4 = "\nThe total number of tasks that haven't been completed and that's overdue is: {}.".format(overdue)
    line5 = "\nThe percentage of tasks that are incomplete is: {}%.".format(percentage_tasks_incomplete)
    line6 = "\nThe percentage of tasks that are overdue is: {}%.".format(percentage_tasks_overdue)

    task_overview_file.write(line0)
    task_overview_file.write(line1)
    task_overview_file.write(line2)
    task_overview_file.write(line3)
    task_overview_file.write(line4)
    task_overview_file.write(line5)
    task_overview_file.write(line6)

    #We then close the file
    task_overview_file.close()


    #Next we work on the user_overview.txt file
    #First we open/create the file and print out the total users and tasks
    user_overview_file = open("user_overview.txt", "w")
    line_head = "\nUser Overview Report"
    line7 = "\nThe toal number of registered users is: {}.".format(total_users)
    line8 = "\nThe total number of tasks generated is {}.".format(total_tasks)

    user_overview_file.write(line_head)
    user_overview_file.write(line7)
    user_overview_file.write(line8)

    #Then for each user we also calculate and print out teh respective stats to the file
    for name in login_names:

        #calcualte the number of tasks assigned to user
        tasks_user_tot=0
        for assign in task_assign:
            if (name == assign):
                tasks_user_tot += 1

        #Calulate the number of complete and incomplete tasks for each user
        tasks_user_complete = 0
        for i, assign in enumerate(task_assign):
            if((name == assign) and (task_completed[i] == "Yes")):
                tasks_user_complete += 1
        
        tasks_user_not_complete = tasks_user_tot - tasks_user_complete

        #calcualte the number of incomplete and overdue tasks for each user
        tasks_user_overdue = 0
        for k, assign in enumerate(task_assign):
            if((name == assign) and (task_completed[k] == "No") and (task_overdue[k] == "Overdue")):
                tasks_user_overdue += 1

        #Calculate the required percentages
        percentage_user_tasks = round((tasks_user_tot/total_tasks),2)
        percentage_complete = round((tasks_user_complete/tasks_user_tot),2)
        percentage_not_complete = round((tasks_user_not_complete/tasks_user_tot),2)
        percentage_overdue = round((tasks_user_overdue/tasks_user_tot),2)

        #Print out results to the user_overview.txt file
        line9 = "\n\nReport for {}:".format(name)
        line10 = "\nTotal number of tasks assigned to {} is: {}.".format(name, tasks_user_tot)
        line11 = "\nPercentage of total tasks assigned to {} is: {}%.".format(name, percentage_user_tasks)
        line12 = "\nPercentage of tasks assigned to {} that is complete is: {}%.".format(name, percentage_complete)
        line13 = "\nPercentage of tasks assigned to {} that is not complete is: {}%.".format(name, percentage_not_complete)
        line14 = "\nPercentage of tasks assigned to {} that is not complete and overdue is: {}%.".format(name, percentage_overdue)

        user_overview_file.write(line9)
        user_overview_file.write(line10)
        user_overview_file.write(line11)
        user_overview_file.write(line12)
        user_overview_file.write(line13)
        user_overview_file.write(line14)


#The below function opens the created task_overview and user_overview text files and prints out
#the contents of each file on screen
def display_report():
    with open('task_overview.txt', 'r') as f:
        lines = [line.rstrip() for line in f]
    for line in lines:
        print(line)

    with open('user_overview.txt', 'r') as f:
        lines = [line.rstrip() for line in f]
    for line in lines:
        print(line)

#First I created empty lists to store the names and passwords of users
login_names = []
login_passwords = []

#next I created empty lists to store the task characteristics
task_assign = []
task_title = []
task_description = []
task_date = []
task_due =[]
task_completed = []

task_set_date = []
task_due_date = []
task_overdue = []

#Create a list of months
months=['January', 'February', 'March', 'April', 'May', 'June', 'July','August',
        'September', 'October', 'November', 'December']

#Here I opened the user.txt file and read in the names and passwords of the users
#This was accordingly assigned to the login_names and login_passwords lists
with open('user.txt', 'r') as f:
    for line in f:
        temp = line.split(",")
        name = temp[0].strip()
        pwd = temp[1].strip()
        login_names.append(name)
        login_passwords.append(pwd)

#Here I opened the tasks.txt file and for each task I appended a characteristic of the task to the respective list 
with open('tasks.txt', 'r') as f:
    for line in f:
        temp = line.split(",")
        assign = temp[0].strip()
        title = temp[1].strip()
        description = temp[2].strip()
        date = temp[3].strip()
        original_date = set_date(date)
        due = temp[4].strip()
        date_due = set_date(due)
        completed = temp[5].strip()

        task_assign.append(assign)
        task_title.append(title)
        task_description.append(description)
        task_date.append(date)
        task_due.append(due)
        task_completed.append(completed)
        task_set_date.append(original_date)
        task_due_date.append(date_due)

        if (original_date > date_due):
            task_overdue.append("Overdue")
        else:
            task_overdue.append("Got Time")

#Here I promted the user for a username
print("Login")
username = input("Username: ")

#Username check, if the username was not registered, I continued to prompt the user for a username
while username not in login_names:
    username = input("Username: ")

#Find index position of username in login_names list
check = login_names.index(username)

#Using this index find the passowrd corresponding to this user
password = input("Password: ")

#Check password, if password does not match then continue to prompt the user for the password
while password != login_passwords[check]:
    password = input("Password: ")

#Display options for user to select - there is an extra statistics option if the user is an admin

options()

#Promt user for a selection from the options menu
selection = input("\nselection: ")

#Execute a while loop that will run as long as the user does not select the exit option
while selection != "e":

    #Here the user can register another user only if the user that is logged on is an admin
    if (selection == "r" and username == "admin"):

        reg_user()

    elif (selection == "r" and username != "admin"):
        print("You are not an administrator!")

    #Here the user can add a task
    #We ask the suer for several inputs and append these to the appropriate task_list
    if(selection == "a"):

        add_task()
        
    #This selection allows the user to view all the tasks
    if (selection == "va"):

        view_all()

    #The below selection prints the tasks assigned to the user that is logged on
    if (selection == "vm"):

        view_mine()

    #Here we show statistics for the number of users and tasks to a user that is logged on as an admin
    if (selection == "ds" and username == "admin"):

        stats()

    #Here we do a check that if a non admin user selects statistics then a message is displayed
    #saying that the user is not an admin
    elif (selection == "ds" and username != "admin"):
        print("You are not an admin!")


    #Here we generate the user_overview and task_overview files for a user that is logged on as an admin
    if (selection == "gr" and username == "admin"):

        generate_report()

    #Here we do a check that if a non admin user selects generate reports then a message is displayed
    #saying that the user is not an admin
    elif (selection == "gr" and username != "admin"):
        print("You are not an admin!")

    #Here we generate the user_overview and task_overview files for a user that is logged on as an admin
    #and display the results on screen for the user to see
    if (selection == "dr" and username == "admin"):
        generate_report()
        display_report()

    #Here we do a check that if a non admin user selects display reusults then a message is displayed
    #saying that the user is not an admin
    elif (selection == "dr" and username != "admin"):
        print("You are not an admin!")


    #If the exit option has not been selected then we diplay
    #options for user to select again - there is an extra statistics option if the user is an admin
    options()
    selection = input("\nselection: ")