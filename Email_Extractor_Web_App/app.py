from flask import Flask,render_template,url_for,request
import re

email_regex = re.compile(r"[\w\.-]+@[\w\.-]+")
# phone_num = re.compile(r"^(?:(?:\+?1\s*(?:[.-]\s*)?)?(?:\(\s*([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9])\s*\)|([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9]))\s*(?:[.-]\s*)?)?([2-9]1[02-9]|[2-9][02-9]1|[2-9][02-9]{2})\s*(?:[.-]\s*)?([0-9]{4})(?:\s*(?:#|x\.?|ext\.?|extension)\s*(\d+))?$")
# phone_num = re.compile(r"^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$")
# phone_num = re.compile(r"^\s*(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})(?: *x(\d+))?\s*$")
phone_num = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
url_https_regex = re.compile(r"https?://www\.?\w+\.\w+")
url_regex = re.compile(r"http?://www\.?\w+\.\w+")

app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/process',methods=["POST"])
def process():
	if request.method == 'POST':
		choice = request.form['taskoption']
		if choice == 'email':
			rawtext = request.form['rawtext']
			results = email_regex.findall(rawtext)
			num_of_results = len(results)
		elif choice == 'phone':
			rawtext = request.form['rawtext']
			results = phone_num.findall(rawtext)
			num_of_results = len(results)
		elif choice == 'url_https':
			rawtext = request.form['rawtext']
			results = url_https_regex.findall(rawtext)
			num_of_results = len(results)
		elif choice == 'url':
			rawtext = request.form['rawtext']
			results = url_regex.findall(rawtext)
			num_of_results = len(results)
		
	
	return render_template("index.html",results=results,num_of_results = num_of_results)


if __name__ == '__main__':
	app.run(debug=True)
