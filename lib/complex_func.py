# from datetime import datetime, date 

# def birthday_checker(str):
#     valid_date_format = True
#     format = "%Y-%m-%d"
#     try:
#         birthday = datetime.strptime(str, "%Y-%m-%d")
#         today = datetime.strptime("2024-02-02", '%Y-%m-%d')
#         age_calc = (today - birthday).days / 365.2425 
#         if int(age_calc) >= 16:
#             return "Access granted"
#         else:
#             return f"Access denied, you are {int(age_calc)} years old. You must be 16 to enter"
#     except ValueError:
#         raise ValueError("Birthday format is invalid")
#     except TypeError:
#         raise TypeError("This date type is invalid")
class DiaryEntry:
    def __init__(self, title, contents):
        # Parameters:
        self.title = title
        #self.contents = contents
        self.content = contents.split()
        #self.new_content_arr = []

    def format(self):
        # Returns:
        return f"My diary entry is about {self.title} and my first content is {self.contents}"
    

    def count_words(self):
        # Returns:
        return len(self.title) + len(self.contents)
        

    # def reading_time(self, wpm):
    #     # Parameters:
    #     #   wpm: an integer representing the number of words the user can read 
    #     #        per minute
    #     self.wpm = wpm
    #     content = self.contents.split()
    #     # Returns:
    #     #   int: an estimate of the reading time in minutes for the contents at
    #     #        the given wpm.
    #     return f"You can read {self.wpm} word per minute so it will take you {int(len(content)/self.wpm)} minutes to complete this diary entry"

    def reading_chunk(self, wpm, minutes):
        # Parameters
        self.wpm = wpm
        self.minutes = minutes
        word_length = self.wpm * self.minutes
        new_content_arr = []
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   string: a chunk of the contents that the user could read in the
        #           given number of minutes
        for x in range(0, word_length - 1):
            new_content_arr.append(self.content[x])
            self.content.pop(x)
        
        return " ".join(new_content_arr)
        #
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that should restart from the beginning.
        
text = "Oluwaseun Jude Ekunayomi Toluhi, I really want to say a big thank you to you. Thank you Thank you Thank you!!! Thank you for being you. Thank you for how much you provide and take care of me. Thank you for apologizing when I’m too stubborn to do so. Thank you for taking situations that I come to you all worked up about, and laying them out for me in this wonderful, logical way that makes everything more clear. Thank you for listening to me and my occasional rants. Thank you for making me laugh when I need it most. Thank you for my new phone 📱 because it was made possible because of you. Thank you for loving my body the way it is, for never making me feel inadequate, but rather perfect for you. Thank you for being on my side when it feels like no one else is. Thank you for making me feel safe."
# content = text.split()
# print(content)
my_diary = DiaryEntry("Love_letter", text)
print(my_diary.reading_chunk(5, 2))
print(my_diary.reading_chunk(5, 2))