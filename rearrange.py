

import re

def rearrange_name(name):
    result = re.search(r"^ *([\w.]*) *, *([\w.]*) *$", name)
    if result is None:
        return name
    return "{} {}".format(result[2], result[1])

import re 
  
my_txt = "An investment in knowledge pays the best interest."

def LetterCompiler(txt):
    result = re.findall(r'([a-c]).', txt)
    return result

print(LetterCompiler(my_txt))