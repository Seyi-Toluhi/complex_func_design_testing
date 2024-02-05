from lib.complex_func import *
# import pytest

# def test_birthday_checker_valid_format():
#     result = birthday_checker("1960-10-21")
#     assert result == "Access granted"


# def test_birthday_checker_invalid_age():
#     result = birthday_checker("2021-10-21")
#     assert result == "Access denied, you are 2 years old. You must be 16 to enter"

# def test_birthday_checker_invalid_format():
    
#     with pytest.raises(Exception) as err:
#         birthday_checker("20-10-7")
#     err_msg = str(err.value)
#     assert  err_msg == "Birthday format is invalid"
    
# def test_birthday_checker_invalid_type_format(): 
#     with pytest.raises(Exception) as err:
#         birthday_checker(1234)
#     err_msg = str(err.value)
#     assert  err_msg == "This date type is invalid"
text = "Oluwaseun Jude Ekunayomi Toluhi, I really want to say a big thank you to you. Thank you Thank you Thank you!!! Thank you for being you. Thank you for how much you provide and take care of me. Thank you for apologizing when I’m too stubborn to do so. Thank you for taking situations that I come to you all worked up about, and laying them out for me in this wonderful, logical way that makes everything more clear. Thank you for listening to me and my occasional rants. Thank you for making me laugh when I need it most. Thank you for my new phone 📱 because it was made possible because of you. Thank you for loving my body the way it is, for never making me feel inadequate, but rather perfect for you. Thank you for being on my side when it feels like no one else is. Thank you for making me feel safe. "

def test_diary_entry_initiated():
    my_diary = DiaryEntry("Holiday", "my Itinerary")
    assert my_diary.title == "Holiday"
    assert my_diary.contents == "my Itinerary"

def test_diary_entry_is_formatted():
    my_diary = DiaryEntry("Holiday", "my Itinerary")
    assert my_diary.format() == "My diary entry is about Holiday and my first content is my Itinerary"

def test_diary_entry_counts_words():
    my_diary = DiaryEntry("Holiday", "my Itinerary")
    assert my_diary.count_words() == 19
    
def test_diary_entry_reading_time():
    my_diary = DiaryEntry("Holiday", "my Itinerary")
    assert my_diary.reading_time(1) == "You can read 1 word per minute so it will take you 2 minutes to complete this diary entry"
    
def test_diary_entry_reading_chunk():
    my_diary = DiaryEntry("Love_letter", text)
    assert my_diary.reading_chunk(5, 2) == "You can read 1 word per minute so it will take you 2 minutes to complete this diary entry"
    