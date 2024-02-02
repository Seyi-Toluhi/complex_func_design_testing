from datetime import datetime, date 

def birthday_checker(str):
    valid_date_format = True
    format = "%Y-%m-%d"
    try:
        birthday = datetime.strptime(str, "%Y-%m-%d")
        today = datetime.strptime("2024-02-02", '%Y-%m-%d')
        age_calc = (today - birthday).days / 365.2425 
        if int(age_calc) >= 16:
            return "Access granted"
        else:
            return f"Access denied, you are {int(age_calc)} years old. You must be 16 to enter"
    except ValueError:
        raise ValueError("Birthday format is invalid")
    except TypeError:
        raise TypeError("This date type is invalid")