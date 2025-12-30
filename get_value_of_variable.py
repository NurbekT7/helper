class Storage:
    def __init__(self):
        self.x = 10
        self.y = 20
    
s = Storage()    
a = input("Write here: ")
        
print(getattr(s, a, "not found"))