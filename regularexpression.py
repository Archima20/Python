import re

result = re.search(r"aza", "plaza")
print(result)
# <re.Match object; span=(2, 5), match='aza'> is what printed 

result= re.search(r"aza", "bazaar")
print(result)
# <re.Match object; span=(2, 5), match='aza'>
# <re.Match object; span=(1, 4), match='aza'>

result= re.search(r"aza", "bammar")
print(result)
# None