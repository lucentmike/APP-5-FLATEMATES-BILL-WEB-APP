from fpdf import FPDF
import webbrowser
import os

class PdfReport:
    """
    Creates a Pdf file that contains data about
    the flatmate such as their names, their due ammount,
    and period of the bill
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):

        flatmate1_pays = str(round(flatmate1.pays(bill=bill, flatmate2=flatmate2), 2))

        flatmate2_pays = str(round(flatmate2.pays(bill=bill, flatmate2=flatmate1), 2))

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        #Add house icon to top
        pdf.image(name = "files/house.png", w=30, h=30)

        #Insert Title 
        pdf.set_font(family='Times', size = 24, style='B')
        pdf.cell(w=0, h=80, txt='Flatmates Bill', border=0, align='C', ln=1)

        #Insert Period label and value
        pdf.set_font(family= "Times", size=14, style ='B')
        pdf.cell(w=100, h=40, txt='Period:', border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        #Insert Name and due Amount of first Flatmate
        pdf.set_font(family="Times", size=12)
        pdf.cell(w=100, h=25, txt=flatmate1.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate1_pays, border=0, ln=1)

        #Insert Name and due Amount of first Flatmate
        pdf.set_font(family="Times", size=12)
        pdf.cell(w=100, h=25, txt=flatmate2.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate2_pays, border=0, ln=1)

        #Change directory, Print the Pdf
        os.chdir("files")
        pdf.output(self.filename)

        #Open PDF automaticlly, if windows : webbrowser.open(self.filename)
        webbrowser.open('file://'+os.path.realpath(self.filename))