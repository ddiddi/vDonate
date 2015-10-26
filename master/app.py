from flask import Flask, render_template, request
from wtforms import Form, BooleanField, TextField, PasswordField,SubmitField, TextAreaField, validators

app = Flask(__name__)

 
class ContactForm(Form):
  name = TextField("Name")
  email = TextField("Email")
  subject = TextField("Subject")
  message = TextAreaField("Message")
  submit = SubmitField("Send")

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()

    if request.method == 'POST':
        return 'Form Posted'

    elif request.method == 'GET':
           return render_template('contact.html', form = form)

    
@app.route('/')
def home_page():
	return render_template('home_page.html')

@app.route('/page')
def company_page():
	dummy = {}
	dummy['balance'] = 10
	dummy['id'] = 42
	dummy['venmoid'] = "test"
	dummy['email'] = 10
	dummy['title'] = 10
	dummy['desc'] = 10
	dummy['domains']= ['asd','asdasdasd']
	l = [1]
	return render_template('company_page.html', company=dummy, l=l)

@app.route('/id')
def id_page():
	return render_template('donate_page.html')

app.run(debug=True)

