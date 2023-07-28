from lib.diary import Diary
from lib.diary_entry import DiaryEntry

"""
Given two entries, returns both entrie from list.
"""

def test_adds_and_lists_two_diary_entries():
    diary = Diary()
    entry_a = DiaryEntry("A Title 1", "Some Contents 1")
    entry_b = DiaryEntry("A Title 2", "Some Contents 2")
    diary.add(entry_a)
    diary.add(entry_b)
    assert diary.all() == [entry_a, entry_b]


"""
Call sum of all the diary entries.
"""

def test_count_words_returns_sum_of_diary_entries():
    diary = Diary()
    entry_a = DiaryEntry("Title 1", "Some Contents")
    entry_b = DiaryEntry("Title 2", "Some More Contents")
    entry_c = DiaryEntry("Title 3", "Lots and Lots More Content")
    diary.add(entry_a)
    diary.add(entry_b)
    diary.add(entry_c)
    assert diary.count_words() == 10


"""
When I add two entries with a totlal of 5 words, when calling
reading_time with a speed of 2 wpm, total should be 3.
"""

def test_reading_time():
    diary = Diary()
    entry_a = DiaryEntry("Title 1", "One two")
    entry_b = DiaryEntry("Title 2", "three four five")
    diary.add(entry_a)
    diary.add(entry_b)
    assert diary.reading_time(2) == 3


"""
Return best entry to fit the amount of reading time.
"""

def test_find_best_entry_for_time():
    diary = Diary()
    entry_a = DiaryEntry("Title 1", "One two three")
    entry_b = DiaryEntry("Title 2", "One two three four five six seven")
    diary.add(entry_a)
    diary.add(entry_b)
    assert diary.find_best_entry_for_reading_time(2, 3) == entry_a

"""
Return single entry to fit the amount of reading time.
"""

def test_find_best_entry_for_time():
    diary = Diary()
    entry_a = DiaryEntry("Title 1", "One two three")
    diary.add(entry_a)
    assert diary.find_best_entry_for_reading_time(2, 3) == entry_a



