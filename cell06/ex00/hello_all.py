import inspect

class myClass:
 def method1(self):
    pass
 def method2(self):
    pass
obj = MyClass()

methode = [name for name, member in inspect.getmembers(obj, prodicate=inspect.ismethod)
    if member.__self__.__class__== MyClass]  
 print("Hello, everyone!")