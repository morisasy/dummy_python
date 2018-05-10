from class_FormatData_CSV import FormatData2
NewData = [FormatData2("George", 65, True),
FormatData2("Sally", 47, False),
FormatData2("Doug", 52, True)]
FormatData2.SaveData("TestFile.csv", NewData)