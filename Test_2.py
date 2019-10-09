import openpyxl

book = openpyxl.load_workbook('Contacts.xlsx')
sheet = book.active
msg = sheet["C1"]
text = msg.value
text = text.split('\n')

for i in range(len(text)):
    print(text[i])