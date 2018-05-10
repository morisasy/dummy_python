class MyClass:
    def DoAdd(self, Value1=0, Value2=0):
        Sum = Value1 + Value2
        print("The sum of {0} plus {1} is {2}.".format(Value1, Value2, Sum))

MyInstance = MyClass()
MyInstance.DoAdd(1, 4)