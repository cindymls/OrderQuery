from flask import Flask, render_template, request, url_for, flash, redirect
from orderquery import *

import random


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

messages = []
@app.route('/', methods=('GET','POST'))
def index():
    if request.method == 'POST':
        orderid = request.form['orderid']
        if not orderid:
          flash('Order number is required!')
        else:
          try:
            status = get_status(orderid)
            messages.clear()
            messages.append(status)
            for message in messages:
              message['Tracking URL'] = message['Tracking URL'].split("'")[1]
              print(message)
            return redirect(url_for('message'))
          except:
            flash('Order number cannot be found.')

            

    return render_template('index.html')

@app.route('/message/')
def message():
  return render_template('message.html', messages=messages)
  
def run():
  app.run(
		host='0.0.0.0',
		port=random.randint(2000,9000)
	)

run()