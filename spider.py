print("Hello World!")

file = open("spider.txt")
print(file.readline())

file = open("spider.txt")
print(file.readline())

print(file.read())

file.close()

with open("spider.txt") as file:
    print(file.readline())

with open("spider.txt") as file:
    for line in file:
        print(line.upper())
        
with open("spider.txt") as file:
    for line in file:
        print(line.strip().upper())
        
