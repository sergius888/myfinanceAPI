import openpyxl

book = openpyxl.Workbook()
sheet = book.active

sheet["A1"] = "hello"
sheet["B1"] = "world!"
sheet["A2"] = "world"
sheet["B2"] = "hello"

sheet.title = "Titlu nou"

# book.save("my.xls")

for row in sheet.rows:
    print(row[0])
