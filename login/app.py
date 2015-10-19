from flask import Flask, render_template

app = Flask(__name__)

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

app.run(debug=True)

