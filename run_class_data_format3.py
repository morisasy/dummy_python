from class_format_data_read_csv import FormatData3
NewData = FormatData3.ReadData("TestFile.csv")
for Entry in NewData:
    print(Entry)