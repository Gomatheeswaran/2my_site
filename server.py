from flask import Flask, render_template

from flask import url_for

from flask import request, redirect

import csv

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about.html")
def about():
     return render_template('about.html')


@app.route("/contact.html")
def contact():
    return render_template("contact.html")

@app.route("/help.html")
def helpu():
    return render_template('help.html')

@app.route("/login.html")
def login():
    return render_template('login.html')

@app.route("/main.html")
def main():
    return render_template('main.html')

@app.route("/packages.html")
def packages():
    return render_template('packages.html')

@app.route("/register.html")
def register():
    return render_template('register.html')

@app.route("/services.html")
def services():
    return render_template('services.html')

def write_to_file(data):
    with open('database.txt', mode ='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n {email}, {subject}, {message}')

def write_to_csv(data):
    with open('database.csv', mode ='a', newline='') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer =csv.writer(database2, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


@app.route("/contact_process.php", methods=['post', 'get'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thank_you.html')
    else:
        return 'something went wrong, Try again!'
