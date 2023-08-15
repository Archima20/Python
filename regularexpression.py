import re

result = re.search(r"aza", "plaza")
print(result)
# <re.Match object; span=(2, 5), match='aza'> is what printed 

result= re.search(r"aza", "bazaar")
print(result)
# <re.Match object; span=(1, 4), match='aza'>

result= re.search(r"aza", "bammar")
print(result)
# None

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
