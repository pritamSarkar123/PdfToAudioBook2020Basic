#pyttsx3 :- python text to speech version x3
#PyPDF2:- to acces the pdf
import pyttsx3
import PyPDF2

#opening in binary format,creating an obj
binaryBook=open('revo2020.pdf','rb')
#binary book reader object
pdfReader=PyPDF2.PdfFileReader(binaryBook)
#count no of pages
noOfPages=pdfReader.numPages
print(noOfPages)

#initializing the speaker
speaker=pyttsx3.init()

for num in range(6,noOfPages):
    # get a page object (0 indexing)
    page = pdfReader.getPage(num)
    # extract the text
    text = page.extractText()
    # speek something
    speaker.say(text)
    # run untill finishes
    speaker.runAndWait()
