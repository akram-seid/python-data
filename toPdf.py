from PyPDF2 import PdfReader
import rereader = PdfReader("crop2.pdf")pageNumber = reader.getNumPages()
for singlePage in range(pageNumber):
    page = reader.getPage(singlePage)
    print(page.extract_text())
    print("************************ " + str(singlePage))print(pageNumber)
