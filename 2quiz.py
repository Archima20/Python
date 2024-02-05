# Module 2 week 3 
# Practice Quiz: Basic Regular Expressions.
# 1.The check_web_address function checks if the text passed qualifies as a top-level web address, meaning that it contains alphanumeric characters (which includes letters, numbers, and underscores), as well as periods, dashes, and a plus sign, followed by a period and a character-only top-level domain such as ".com", ".info", ".edu", etc. Fill in the regular expression to do that, using escape characters, wildcards, repetition qualifiers, beginning and end-of-line characters, and character classes.
import re
def check_web_address(text):
    pattern = r"^[a-zA-Z0-9._+-]+\.[a-zA-Z]+$"
    result = re.search(pattern, text)
    return result is not None

print(check_web_address("gmail.com"))  # True!
print(check_web_address("www@google"))  # False
print(check_web_address("www.Coursera.org"))  # True!
print(check_web_address("web-address.com/homepage"))  # False
print(check_web_address("My_Favorite-Blog.US"))  # True


# 2.The check_time function checks for the time format of a 12-hour clock, as follows: the hour is between 1 and 12, with no leading zero, followed by a colon, then minutes between 00 and 59, then an optional space, and then AM or PM, in upper or lower case. Fill in the regular expression to do that. How many of the concepts that you just learned can you use here?
import re
def check_time(text):
  pattern = r'^([0-9]|1[0-2]):[0-5][0-9]\s?(AM|am|PM|pm)$'
  result = re.search(pattern, text)
  return result != None

print(check_time("12:45pm")) # True
print(check_time("9:59 AM")) # True
print(check_time("6:60am")) # False
print(check_time("five o'clock")) # False

# ^: Matches the start of the string.
#([0-9]|1[0-2]): Matches the hour in 12-hour format, either a single digit or a two-digit number from 1 to 12.
#:: Matches a colon (used to separate hours and minutes).
# [0-5][0-9]: Matches the minutes, ensuring they are in the range of 00 to 59.
# \s?: Matches zero or one whitespace character (optional space).
#So, \s? in the pattern allows for optional whitespace. It means that the regular expression is looking for a time in the format "hh:mm" followed by an optional space and an AM/PM indicator.
#(AM|am|PM|pm): Matches either "AM," "am," "PM," or "pm" for the time of day.
# $: Matches the end of the string.

# 4.The transform_comments function converts comments in a Python script into those usable by a C compiler. This means looking for text that begins with a hash mark (#) and replacing it with double slashes (//), which is the C single-line comment indicator. For the purpose of this exercise, we'll ignore the possibility of a hash mark embedded inside of a Python command, and assume that it's only used to indicate a comment. We also want to treat repetitive hash marks (##), (###), etc., as a single comment indicator, to be replaced with just (//) and not (#//) or (//#). Fill in the parameters of the substitution method to complete this function:
import re
def transform_comments(line_of_code):
  result = re.sub(r'(#+)','//', line_of_code)
  return result

print(transform_comments("### Start of program")) 
# Should be "// Start of program"
print(transform_comments("  number = 0   ## Initialize the variable")) 
# Should be "  number = 0   // Initialize the variable"
print(transform_comments("  number += 1   # Increment the variable")) 
# Should be "  number += 1   // Increment the variable"
print(transform_comments("  return(number)")) 
# Should be "  return(number)"

#5.The convert_phone_number function checks for a U.S. phone number format: XXX-XXX-XXXX (3 digits followed by a dash, 3 more digits followed by a dash, and 4 digits), and converts it to a more formal format that looks like this: (XXX) XXX-XXXX. Fill in the regular expression to complete this function.

import re
def convert_phone_number(phone):
  result = re.sub(r'(\b\d{3})-(\d{3}-\d{4})\b',r'(\1) \2', phone)
  return result

print(convert_phone_number("My number is 212-345-9999.")) # My number is (212) 345-9999.
print(convert_phone_number("Please call 888-555-1234")) # Please call (888) 555-1234
print(convert_phone_number("123-123-12345")) # 123-123-12345
print(convert_phone_number("Phone number of Buckingham Palace is +44 303 123 7300")) # Phone number of Buckingham Palace is +44 303 123 7300

