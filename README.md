# PDF-Auto-Reader 
Convert PDF File Text to Audio Speech using Python.
Let us see how to read a PDF that is converting a textual PDF file into audio.

Packages Used:

1)pyttsx3: It is a Python library for Text to Speech. It has many functions which will help the machine to communicate with us. It will help the machine to speak to us
2)PyPDF2: It will help to the text from the PDF. A Pure-Python library built as a PDF toolkit. It is capable of extracting document information, splitting documents page by page, merging documents page by page etc.
Both these modules need to be installed

- pip install pyttsx3
- pip install PyPDF2
You also need to know about the open() function which will help us to open the PDF in read mode. Knowledge about the OOPS Concept is also recommended.

APPROACH :


1) Import the PyPDF2 and pyttx3 modules.
2) Open the PDF file.
3) Use PdfFileReader() to read the PDF. We just have to give the path of the PDF as the argument.
4) Use the getPage() method to select the page to be read.
5) Extract the text from the page using extractText().
6) Instantiate a pyttx3 object.
7) Use the say() and runwait() methods to speak out the text.

# Enjoy the Code By Shalin ! 

