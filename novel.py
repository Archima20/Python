with open("novel.txt", "a") as file:
    file.write("It was a  dark and stormy night")
    
with open("novel.txt") as file:
    file.read()
    print(file.readline())