import requests
import sys
import os
import base64
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash, json, jsonify
import redis
from PIL import Image
import StringIO


conn = redis.Redis('localhost')
app = Flask(__name__)


@app.route('/app', methods=['GET'])
def home():
	
    return render_template('index.html')

@app.route('/app/<keyword>')
def imageCache(keyword):
	print keyword
	if(conn.get(keyword)):
		img = conn.get(keyword)
		tempBuff = StringIO.StringIO()
		tempBuff.write(img)
		tempBuff.seek(0) #need to jump back to the beginning before handing it off to PIL
		jpgfile=Image.open(tempBuff)
		#image1 = base64.b64encode(img)
		#img.encode("base64")
		output = StringIO.StringIO()
		jpgfile.save(output, format='PNG')
		output.seek(0)
		output_s = output.read()
		b64 = base64.b64encode(output_s)
		return render_template('index.html', key="cache",image=b64)
	else:
		if keyword=="CMPE_Building9":
			jpgfile = Image.open("./static/img/image_cmpe_building.png")
			conn.set(keyword,jpgfile)
		#	image2 = base64.b64encode(jpgfile)
			#jpgfile.encode("base64")
			output = StringIO.StringIO()
			jpgfile.save(output, format='PNG')
			output.seek(0)
			output_s = output.read()
			b64 = base64.b64encode(output_s)

		elif keyword=="image_library":
			jpgfile = Image.open("./static/img/image_library.png")
			conn.set(keyword,jpgfile)
		#	image2 = base64.b64encode(jpgfile)
			#jpgfile.encode("base64")
			output = StringIO.StringIO()
			jpgfile.save(output, format='PNG')
			output.seek(0)
			output_s = output.read()
			b64 = base64.b64encode(output_s)
		elif keyword=="image_sjsu":
			jpgfile = Image.open("./static/img/image_sjsu.png")
			conn.set(keyword,jpgfile)
		#	image2 = base64.b64encode(jpgfile)
			#jpgfile.encode("base64")
			output = StringIO.StringIO()
			jpgfile.save(output, format='PNG')
			output.seek(0)
			output_s = output.read()
			b64 = base64.b64encode(output_s)

		return render_template('index.html',key="db", image=b64)	
   

port = os.getenv('VCAP_APP_PORT', '8000')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(port), debug=True)

