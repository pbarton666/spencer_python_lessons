class Dogma(int):
    def __init__(self, value):
        self.value=value
    def __add__(self, value):
        print("bark!", value)
        
dog = Dogma(1)
print(dog+1)
