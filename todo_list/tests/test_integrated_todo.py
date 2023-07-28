from lib.todo import Todo
from lib.todo_list import TodoList
import pytest

"""
Test create a task and mark it complete.
"""

def test_enter_single_task():
    my_list = TodoList()
    task1 = Todo("Learn TDD")
    my_list.add(task1)
    assert my_list.incomplete() == [task1]

"""
Test create multiple tasks
"""

def test_enter_multiple_tasks():
    my_list = TodoList()
    task1 = Todo("Learn TDD")
    task2 = Todo("Buy Beer")
    task3 = Todo("Drink Beer")
    my_list.add(task1)
    my_list.add(task2)
    my_list.add(task3)
    assert my_list.incomplete() == [task1, task2, task3]

"""
Test a single test is marked complete
"""

def test_task_is_marked_complete():
    my_list = TodoList()
    task1 = Todo("Get Beer")
    my_list.add(task1)
    task1.mark_complete()
    assert my_list.complete() == [task1]
    

"""
Test create multiple tasks and mark complete.
"""

def test_enter_multiple_tasks_are_complete():
    my_list = TodoList()
    task1 = Todo("Learn TDD")
    task2 = Todo("Buy Beer")
    task3 = Todo("Drink Beer")
    my_list.add(task1)
    my_list.add(task2)
    my_list.add(task3)
    task1.mark_complete()
    task2.mark_complete()
    task3.mark_complete()
    assert my_list.complete() == [task1, task2, task3]

"""
Test mark all complete aka give_up.
"""

def test_enter_multiple_tasks_are_complete():
    my_list = TodoList()
    task1 = Todo("Learn TDD")
    task2 = Todo("Buy Beer")
    task3 = Todo("Drink Beer")
    my_list.add(task1)
    my_list.add(task2)
    my_list.add(task3)
    my_list.give_up()
    assert my_list.complete() == [task1, task2, task3]

    