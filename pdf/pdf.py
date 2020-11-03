from PyPDF2 import PdfFileWriter, PdfFileReader

input1 = PdfFileReader(open("/Users/riarosenauer/Library/Mobile Documents/com~apple~CloudDocs/Ria/Website/FS/FS_website/pdf/Ex2_Blatt1_Lösung.pdf", "rb"))

# analyze pdf data
print(input1.getDocumentInfo())
print(input1.getNumPages())
text = input1.getPage(0).extractText()
print("")
print(type(input1.getPage(0)))
print("")
print("")
print(text.encode("windows-1250", errors='backslashreplacee'))
print("")
print(type(text))

# create output document
output = PdfFileWriter()
output.addPage(input1.getPage(0))
fout = open("/Users/riarosenauer/Library/Mobile Documents/com~apple~CloudDocs/Ria/Website/FS/FS_website/pdf/Ex2_Blatt1_Lösung2.pdf", "wb")
output.write(fout)
fout.close()