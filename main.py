from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template, request
from wtforms.fields.core import Label
from flatmates_bill import flat

#Creates the Flask app
app = Flask(__name__)


#Creates the pages, using get method to call page
class HomePage(MethodView):
    
    def get(self):
        return render_template('index.html')

class BillFormPage(MethodView):
    def get(self):
        bill_form = BillForm()
        return render_template('bill_form_page.html', billform=bill_form)

#Creates a results page method that posts the out to the webpafe. Uss tehe request.form to pull information from the form
class ResultsPage(MethodView):
    def post(self):
        billform = BillForm(request.form)

        the_bill = flat.Bill(float(billform.amount.data), billform.period.data)
        flatmate1 = flat.Flatmate(name = billform.name1.data, days_in_house= float(billform.days_in_house1.data))
        flatmate2 = flat.Flatmate(name = billform.name2.data, days_in_house= float(billform.days_in_house2.data))

        return render_template('results.html', name1 = flatmate1.name, amount1 = flatmate1.pays(the_bill, flatmate2), name2 = flatmate2.name, amount2 = flatmate2.pays(the_bill, flatmate1))

#Creates the bill form that inherits from the wtforms, forms. 
class BillForm(Form):
    amount = StringField(label = 'Bill Amount: ' , default = 100)
    period = StringField(label= 'Bill Period: ' , default = 'December' )

    name1 = StringField(label = 'Name: ', default = "Mike")
    days_in_house1 = StringField(label = 'Days in House: ' , default = 20)

    name2= StringField(label = 'Name: ' , default = "Kylie")
    days_in_house2 = StringField(label = 'Days in House: ' , default = 15)

    button = SubmitField('Calculate')


#Adds URL rules, when the URL is called, load the page and page name
app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/bill_form', view_func=BillFormPage.as_view('bill_form_page'))
app.add_url_rule('/results', view_func=ResultsPage.as_view('results_page'))

app.run(debug=True)