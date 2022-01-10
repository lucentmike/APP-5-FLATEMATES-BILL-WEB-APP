from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template
from wtforms.fields.core import Label

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

class ResultsPage(MethodView):
    pass

class BillForm(Form):
    amount = StringField(label = 'Bill Amount: ')
    period = StringField(label= 'Bill Period: ')

    name1 = StringField(label = 'Name: ')
    days_in_house1 = StringField(label = 'Days in House: ')

    name2= StringField(label = 'Name: ')
    days_in_house2 = StringField(label = 'Days in House: ')

    button = SubmitField('Calculate')


#Adds URL rules, when the URL is called, load the page and page name
app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/bill_form', view_func=BillFormPage.as_view('bill_form_page'))

app.run(debug=True)