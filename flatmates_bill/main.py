from flat import Bill, Flatmate
from reports import PdfReport

the_bill = Bill(amount = float(input("Ender the total bill amount: ")) , period = input("Enter the bill period: "))
flatmate1 = Flatmate(name=input("Enter flatmate 1 name: ") , days_in_house= float(input("Enter flatmate 1 days in house: ")))
flatmate2 = Flatmate(name=input("Enter flatmate 2 name: "), days_in_house= float(input("Enter flatmate 2 days in house: ")))

print(flatmate1.name, "Pays: ", flatmate1.pays(bill=the_bill, flatmate2=flatmate2))
print(flatmate2.name, "Pays: ", flatmate2.pays(bill=the_bill, flatmate2=flatmate1))

pdf_report = PdfReport(filename  = f"{the_bill.period}.pdf")
pdf_report.generate(flatmate1=flatmate1, flatmate2= flatmate2, bill=the_bill)