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