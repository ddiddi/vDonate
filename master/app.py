from flask import Flask, render_template

app = Flask(__name__)
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

