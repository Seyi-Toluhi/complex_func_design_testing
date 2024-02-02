# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

As an admin
So that I can determine whether a user is old enough
I want to allow them to enter their date of birth as a string in the format `YYYY-MM-DD`.

As an admin
So that under-age users can be denied entry
I want to send a message to any user under the age of 16 saying their access is denied, telling them their current age and the required age (16).

As an admin
So that old enough users can be granted access
I want to send a message to any user aged 16 or older to say that access has been granted.

As an admin
So that invalid entries are rejected
I want to generate an exception when the date of birth isn't the right type or format.


## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE
def birthday_checker():
    #one parameter i.e str
    #convert str to a date
    #calculate age by comapring to current date
    #compare age
    # return a string as a msg to user as access granted or not

```
## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE
"""
check when the date of birth is given in a correct str format

"""
test_birthday_checker_valid_format():
    result = birthday_checker("1960-10-21")
    assert result == True 

"""
checking that an underage user is denied entry
"""

test_birthday_checker_valid_format():
    result = birthday_checker("2020-11-21")
    assert result == "Access denied, you are 3 years old. Access age is 16."
```
_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE


```

Ensure all test function names are unique, otherwise pytest will ignore them!
