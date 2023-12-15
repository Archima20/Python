class Field: 
    def __init__(self) -> None:
        self.data = [" " for i in range(9)]
        self.next = "X"
        
    def print(self):
        print(f"{self.data[0]}|{self.data[1]}|{self.data[2]}")
        print("-+-+-")
        print(f"{self.data[3]}|{self.data[4]}|{self.data[5]}")
        print("-+-+-")
        print(f"{self.data[6]}|{self.data[7]}|{self.data[8]}")

    def put(self, index: int):
        if index<len(self.data) and index>=0 and self.data[index]== " ":
            self.data[index]= self.next
            self.next= "O" if self.next=="X" else "X"
            
    def checkwinner(self):
        for p in ["X" , "O"]:
            for i in [0, 3 ,6 ]:
                if self.data[i] == p and self.data[i+1] == p and self.data[i+2] == p :
                    return p
                
            for i in [0, 1 ,2]:
                if self.data[i] == p and self.data[i+3] == p and self.data[i+6] == p :
                    return p
        
    
    
if __name__ == "__main__":
    field= Field()
    while True :
        i= input(f"{field.next} make a move:")
        i= int(i)
        field.put(i)
        field.print()
        if field.checkwinner() == " ":
            continue
        else:
            print(f"{field.checkwinner()} has won!")
            break
    