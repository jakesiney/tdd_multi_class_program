from lib.todo import Todo

class TodoList:
    def __init__(self):
        self.todos = []
        
    def add(self, todo):
        self.todos.append(todo)
      
    def incomplete(self):
        return [todo for todo in self.todos if not todo.complete]

    def complete(self):
        return [todo for todo in self.todos if todo.complete]

    def give_up(self):
        """Sets the complete property of all todos in the list to True."""
        for todo in self.todos:
            todo.mark_complete()



# todo_list = TodoList()
# todo1 = Todo("Buy groceries")
# todo2 = Todo("Clean the house")
# todo3 = Todo("Do the laundry")

# todo_list.add(todo1)
# todo_list.add(todo2)
# todo_list.add(todo3)

# print(todo_list.incomplete())
# # ['Buy groceries', 'Clean the house', 'Do the laundry']

# todo_list.give_up()

# print(todo_list.incomplete())
# # []
