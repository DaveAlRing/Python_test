class Math:
    @staticmethod
    def add5(x):
        return x + 5
    
class Text:
    @staticmethod
    def phrase():
        return "This is a static method"
    
print(Math.add5(5))

print(Text.phrase())
