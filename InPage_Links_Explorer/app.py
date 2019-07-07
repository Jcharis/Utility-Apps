from flask import Flask,render_template,request,jsonify
import urllib.request
import re
import socket
from collections import Counter
# from urllib.request import Request, urlopen

# req = Request('', headers={'User-Agent': 'Mozilla/5.0'})
# webpage = urlopen(req).read()

# REGEX
https_regex = re.compile(r"https?://www\.?\w+\.\w+")
http_regex = re.compile(r"http?://www\.?\w+\.\w+")

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/analyze',methods=['GET','POST'])
def analyze():
	if request.method == 'POST':
		raw_url = request.form['main_url']
		f = urllib.request.urlopen(raw_url)
		# Get Raw HTML
		# print(f.read())
		# URL
		target_url = f.geturl()
		# Get IP
		domain_name = target_url.split('/')[2]
		hostip = socket.gethostbyname(domain_name)
		httplinks = http_regex.findall(str(f.read()))
		httpslinks = https_regex.findall(str(f.read()))
		links_freq_https = Counter(httpslinks)
		links_freq_http = Counter(httplinks)
		print(httpslinks)
		print(httplinks)


	return render_template('index.html',raw_url=raw_url,target_url=target_url,domain_name=domain_name,hostip=hostip,httpslinks=httpslinks,httplinks=httplinks,links_freq_https=links_freq_https,links_freq_http=links_freq_http)



if __name__ == '__main__':
	app.run(debug=True)