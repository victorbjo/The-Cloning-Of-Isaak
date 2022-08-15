class base():
    def __init__(self) -> None:
        self.asd = 2
        pass
    def doTheThing(self):
        print("I'm doing the thing! ", self.asd)
class stats():
    def __init__(self) -> None:
        self.asd = 2
        pass
    def doTheThing(self):
        self.asd -= 1
    
class child(base):
    def __init__(self) -> None:
        self.stats = stats()
        super().__init__()
        self.asd = 3
        
test = child()
print(test.stats.asd)
test.stats.doTheThing()
print(test.stats.asd)