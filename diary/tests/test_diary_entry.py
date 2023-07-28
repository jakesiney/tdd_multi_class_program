from lib.diary_entry import DiaryEntry

"""
Initialise with a title and entry, then return the title and contents back.
"""
def test_data_entry_and_get_title_entry_from_lists():
    diary_entry = DiaryEntry
    diary_entry.title = "Title"
    diary_entry.contents = "An Entry"


def test_count_list_words():
    diary_entry = DiaryEntry("Title", "one two three four five")
    assert diary_entry.count_words() == 5
