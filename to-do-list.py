# to do list in Python
# 3 lists: To do, In progress, & Completed

def printLists():
    # print lists
    # this code needs tidying
    # tabulate?
    print('IN PROGRESS:)
    for item in inprog_list:
          print(item)
    print('TO DO:')
    for item in todo_list:
        print(item)
    print('RECENTLY COMPLETED:')
          for item in compl_list:
          print(item)
     print(' ')
def updateLists():
    # move items between lists
    # if move makes length of completed items > 5, delete oldest (del compl_list[0])
    
# make lists to hold on to items
todo_list = []
inprog_list = []
compl_list = []

# print out instructions on how to use the app
helpInfo_str = 'Enter "SHOW" to display lists, "UPDATE" to move an item to another list, "HELP" to show this line and "DONE" when finished'
print('Add an item to TO DO list:')
print(helpInfo_str)

while True:
    # ask for new items
    new_item = input('> ')
    
    if new_item == 'DONE':
        break
    elif new_item == 'SHOW':
        printLists()

    elif new_item == 'HELP':
        print(helpInfo_str)
    elif new_item == 'UPDATE':
        updateLists()
    
    #add new item to list
    else:
        todo_list.append(new_item)
        print('Added {}. To Do list now has {} items.'.format(new_item, len(todo_list)))
        
#print out the lists
printLists()