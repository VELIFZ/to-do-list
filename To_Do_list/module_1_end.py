# Add tasks
# View tasks
# Delete tasks
# Quit the application
# store input result in list

# Implement error handling using try, except, else, and finally blocks to catch errors
# Alert the user if they provide invalid input
# Alert the user if there are no tasks to view
# Alert the user if they try to delete a task that doesn't exist
# Alert the user if they select an option on the main menu that doesn't exist


tasks = []

def add():
    try:
        while True:
            # add strip if only bunch of spaces were entered
            add_ask = input("Add a task in your to-do list (type 'done' to end): \n").strip().capitalize()
            # empty input error handle - if bunch of space was the answer raise error. 
            if (len(add_ask) == 0):
            #if not add_ask:
                raise ValueError('Add something valid to your list')
            # break so we don't have endless responses
            elif add_ask.lower() == 'done':
                break
            # finally add the responses to the list
            else:
                tasks.append(add_ask)
        print(tasks)
        
        # this code for if list is empty- because if done is the first answer output is ->[]
        #? can I leave it that way, an empty list?
        if (tasks == []):
            print('The list is empty!')
    # exception for only empty input
    except ValueError as e:
        print(e)
        #! continue to call the function after this error. otherwise it ends after giving the error message
        add() 
    # another except for other errors that wasn't predicted 
    except Exception as e:
        print(f'An error occurred: {e}')

#add()

# See all the tasks under each other with the order they were entered. 
# starts = 1 since I don't task number 0
def view():
    if tasks == []:
        print("You have no tasks in your to-do list.")
    for index, task in enumerate(tasks, start=1):
        print(f'{index}. {task}')      
#view()


# 
def delete():
    delete_t = int(input('Get rif of the task. Enter the task number: ').strip())
    # if number is not in the list 
    try:
        if (delete_t < 1) or (delete_t > len(tasks)):
            raise IndexError('Give the exact number of the task you want remove from the list.')
        tasks.pop(delete_t - 1)
        print(tasks)
    except IndexError as e:
        # call the function again because stops after the error
        delete()
        print(e)
    except Exception as e:
        print(f'An error occurred: {e}')
#delete()

# main is shows user how they can do stuff to their list
def main():
    while True:
        # i know so many \n :(
        option = int(input('\nWhat do you want to do? n\Enter one of these number \n1. Add Tasks \n2. View Tasks \n3. Delete Task \n4. Quit \n').strip())
        if option == 1:
            add()
        elif option == 2:
            view()
        elif option == 3:
            delete()
        elif option == 4:
            break
        else:
            print("Choose one of the above numbers.")
main()
