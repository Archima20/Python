import re

result = re.search(r"aza", "plaza")
print(result)
# <re.Match object; span=(2, 5), match='aza'> is what printed 

result= re.search(r"aza", "bazaar")
print(result)
# <re.Match object; span=(1, 4), match='aza'>

result= re.search(r"aza", "bammar")
print(result)
# None is the answer

print(re.search(r"^x", "xenian"))
# <re.Match object; span=(0, 1), match='x'>

print(re.search(r"p.ng", "penguin"))
# <re.Match object; span=(0, 4), match='peng'>

print(re.search(r"p.ng", "clapping"))
# <re.Match object; span=(3, 8), match='ping'>

print(re.search("p.ng", "spong"))
#<re.Match object; span=(1, 5), match='pong'>

print(re.search(r"p.ng", "pangea", re.IGNORECASE))
# <re.Match object; span=(0, 4), match='pang'>

print(re.search(r"[pP]ython", "python"))
# <re.Match object; span=(0, 6), match='python'>

print(re.search(r"[a-z]way", "The end of the highway"))
# <re.Match object; span=(18, 22), match='hway'>

print(re.search(r"[a-z]way", "what a way to go"))
# None

print(re.search(r"[aA-Zz]", "what is the correct way? I really wanna know! tell me plase."))
# <re.Match object; span=(2, 3), match='a'>

print(re.search(r"[aA-Zz]way", "what a way to go"))
None

print(re.search(r"cat|dog", "Happy is a dog."))
# <re.Match object; span=(11, 14), match='dog'>

print(re.search(r"cat|dog", "Happy are our cats not dog."))
# <re.Match object; span=(13, 16), match='cat'>

print(re.findall(r"cat|dog", "Happy are our cats not dog."))
# ['cat', 'dog']

print(re.search(r"Py.*n", "Python pygmalion"))
# <re.Match object; span=(0, 16), match='Python pygmalion'> ?

print(re.search(r"Py.*n", "Python programming language"))
# <re.Match object; span=(0, 22), match='Python programming lan'> ??

print(re.search(r"Py[a-z]*n", "Python programming language"))
# <re.Match object; span=(0, 6), match='Python'>

print(re.search(r"Py[a-z]*n", "Pyn"))
#<re.Match object; span=(0, 3), match='Pyn'>

print(re.search(r"Py[a-z]*n", "Pythrg"))
# None

print(re.search(r"o+l+", "woolly"))
# <re.Match object; span=(1, 5), match='ooll'>

print(re.search(r"o+l+", "boil"))
# None

print(re.search(r"p?each", "I love peaches"))
# <re.Match object; span=(7, 12), match='peach'>

print(re.search(r"p?each", "I love eaches"))
# <re.Match object; span=(7, 11), match='each'>

import re
def repeating_letter_a(text):
  result = re.search(r"___", text)
  return result != None
# I could not answer this exercise! 

print(re.search(r".com", "welcome"))
# <re.Match object; span=(2, 6), match='lcom'>

print(re.search(r"\.com", "welcome"))
#None

print(re.search(r"ne.*t", "net next time success"))
# <re.Match object; span=(0, 10), match='net next t'>

print(re.findall(r"[aA]l.*n", "Allign all possible allignment in alligning line"))
# ['Allign all possible allignment in alligning lin']

print(re.search(r".com", "welcome TO the welcoming center"))
#<re.Match object; span=(2, 6), match='lcom'>

print(re.findall(r".com", "welcome TO the welcoming center"))
# ['lcom', 'lcom']

print(re.findall(r".com", "welcome TO the welcoming center on booking.com"))
# ['lcom', 'lcom', '.com']

#I need to practice more and more 
#I have to focus on this course, I recevieved the second notice that they will drop me out!

print(re.search("/.com", "welcome here."))
#none "escaping chareccter"

print(re.search(r"/w*", "welcome here."))
# none
print(re.search(r"\w*", "This is an example."))
# <re.Match object; span=(0, 4), match='This'>

print(re.search(r"\w*", "This_is_an_example."))
# <re.Match object; span=(0, 18), match='This_is_an_example'>

print(re.search(r"\S*", "This_is_an_example."))
#<re.Match object; span=(0, 19), match='This_is_an_example.'>

print(re.search(r"\S*", "This is an example."))
# <re.Match object; span=(0, 4), match='This'>

import re
def check_character_groups(text):
  result = re.search(r"\w+\s+\w+", text)
  return result != None

print(check_character_groups("One")) # False
print(check_character_groups("123  Ready Set GO")) # True
print(check_character_groups("username user_01")) # True
print(check_character_groups("shopping_list: milk, bread, eggs.")) # False

pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
print(re.search(pattern, "_this_is_a_valid_variable"))
#<re.Match object; span=(0, 25), match='_this_is_a_valid_variable'>


import re
def check_sentence(text):
  result = re.search(r"^[A-Z][a-z\s]*[.!?]$", text)
  return result != None

print(check_sentence("Is this is a sentence?")) # True
print(check_sentence("is this is a sentence?")) # False
print(check_sentence("Hello")) # False
print(check_sentence("1-2-3-GO!")) # False
print(check_sentence("A star is born.")) # True

import re
def rearrange_name(name):
  result = re.search(r"^(\w*), (\w*)$", name)
  if result == None:
    return name
  return "{} {}".format(result[2], result[1])

name=rearrange_name("Kennedy, John F.")
print(name)

import re

def rearrange_name(name):
    # The pattern now matches last name, first name, optional middle name/initial, and optional double surnames.
    result = re.search(r"^(\w*), (\w*)(?: (\w*\.?|\w*))?$", name)
    
    if result is None:
        return name
    
    last_name = result.group(1)
    first_name = result.group(2)
    middle_name = result.group(3) or ""  # Handle the case when there's no middle name/initial.
    
    # Combine the components into the desired format.
    rearranged_name = "{} {}{}".format(first_name, middle_name, last_name)
    
    return rearranged_name

name = rearrange_name("Kennedy, John F.")
print(name)
