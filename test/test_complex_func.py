from lib.complex_func import *
import pytest

def test_birthday_checker_valid_format():
    result = birthday_checker("1960-10-21")
    assert result == "Access granted"


def test_birthday_checker_invalid_age():
    result = birthday_checker("2021-10-21")
    assert result == "Access denied, you are 2 years old. You must be 16 to enter"

def test_birthday_checker_invalid_format():
    
    with pytest.raises(Exception) as err:
        birthday_checker("20-10-7")
    err_msg = str(err.value)
    assert  err_msg == "Birthday format is invalid"
    
def test_birthday_checker_invalid_type_format(): 
    with pytest.raises(Exception) as err:
        birthday_checker(1234)
    err_msg = str(err.value)
    assert  err_msg == "This date type is invalid"