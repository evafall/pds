from flask import Flask,render_template,request
from notifications import send_email

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/single',methods=['GET','POST'])
def single():
    fname = request.form['fname']
    lname = request.form['lname']
    email = request.form['email']
    subject = request.form['subject']
    message = request.form['message']

    data = [fname,lname,email,subject,message]

    subject = "Enquiry"
    fileToSend = None
    msgg = " First Name : "+fname+" \n Last Name : "+lname+" \n Email : "+email+" \n Subject : "+subject+"  \n Message : "+message+"  "

    toaddr = "pdesignstudio7@gmail.com"
    send_email(msgg,subject,toaddr,fileToSend)

    return render_template('index.html')

if __name__ == '__main__':
   app.run(debug=True)
