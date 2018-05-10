import class_Person
SamsRecord = class_Person.MyClass()
AmysRecord = class_Person.MyClass("Amy", 44)
print(SamsRecord.GetAge())
SamsRecord.SetAge(33)
print(AmysRecord.GetName())
AmysRecord.SetName("Aimee")
print(SamsRecord)
print(AmysRecord)