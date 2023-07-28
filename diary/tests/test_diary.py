from lib.diary import Diary

"""
Return list of entries, list is empty.
"""
def test_zero_entries():
    diary = Diary()
    assert diary.all() == []

"""
Show initial word count is 0
"""

def test_initial_word_count():
    diary = Diary()
    assert diary.count_words() == 0

"""

"""