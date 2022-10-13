from openpyxl import load_workbook

book = load_workbook("Book1.xlsx")
ws = book.worksheets[0]


def saveToExcel():
    ws.cell(row=count, column=1).value = last_object.chat_id
    ws.cell(row=count, column=2).value = last_object.name
    ws.cell(row=count, column=3).value = last_object.id_no
    ws.cell(row=count, column=4).value = last_object.last_word
    book.save("Book1.xlsx")
    os.execv(sys.argv[0], sys.argv)
