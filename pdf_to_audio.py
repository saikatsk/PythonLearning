# Following packages are required
# PyPDF2 - Pdf to text converter library
# sudo pip3 install PyPDF2
# pyttsx3 - text to speech converter library
# sudo pip3 install pyttsx3
# tkinter - Python equivalent of Tcl/Tk
# This library is used for GUI apps
# sudo apt-get install python3-tk
# espeak - this library works with pyttsx3 in linux
# sudo apt-get install python3-espeak

import pyttsx3
import PyPDF2
from tkinter.filedialog import *

book = askopenfilename()
pdfreader = PyPDF2.PdfFileReader(book)
pages = pdfreader.numPages

for num in range(0, pages):
    page = pdfreader.getPage(num)
    text = page.extractText()
    print('Text retrieved = ' + text)
    player = pyttsx3.init()
    #player.say(text)
    player.say("Install espeak and the python-espeak package in Ubuntu with apt-get.")
    player.runAndWait()
