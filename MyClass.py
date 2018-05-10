class MyClass:
    Greeting = ""
    def __init__(self, Name="there"):
        self.Greeting = Name + "!"
    def SayHello(self):
        print("Hello {0}".format(self.Greeting))
        
MyInstance = MyClass()
MyInstance.SayHello()
MyInstance2 = MyClass("Amy")
MyInstance2.SayHello()

MyClass.Greeting = "Zelda"

MyClass.Greeting
