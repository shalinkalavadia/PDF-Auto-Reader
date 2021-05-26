import pyttsx3    # write pip install pyttsx3 in terminal
import PyPDF2      # write pip install PyPDF2 in terminal
pdf  = open('cv_template_sheet_en.pdf','rb') #write the file name of pdf you want to read
Reader = PyPDF2.PdfFileReader(pdf)
total_pages = Reader.numPages
#name= Reader.namedDestinations
#print(name)
print(total_pages)


#use for loop and provide range if want to read all the pages

page=Reader.getPage(0)
text=page.extractText()


speaker = pyttsx3.init()
speaker.say('hello , i will be reading for you ')
speaker.say(text)
speaker.runAndWait()