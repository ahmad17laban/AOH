from flask import Flask, render_template,request,session, url_for,redirect
from flask_mail import Mail, Message
from waitress import serve
import secrets 
import os
from data import storeData,readData
secrets.token_hex(16)


app = Flask(__name__)
app.secret_key = 'fbd1_efad885bf@35e1d5ea08424xenel221'


# email configeration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
# put your email 
app.config['MAIL_USERNAME'] = 'basabrain.am@gmail.com'
# put the web password from gmail service
app.config['MAIL_PASSWORD'] = 'sukftpyoafpwiuei'

mail = Mail(app)







@app.route("/")
@app.route("/index.html")
@app.route("/index")
def home():
    return render_template('index.html', title='Home')


@app.route('/handle_email',methods=['GET','POST'])
def handle_email():
    name = request.form['name_us']
    phone= request.form['phone_us']
    email = request.form['email_us']
    texarea= request.form['text_us']
    msg=Message(f"Message {email}",recipients=['basabrain.am@gmail.com'],sender=email)
    msg.body= f''' {name} said {texarea} '''
    mail.send(msg) 
    return redirect('index.html') 


if __name__ == '__main__':
    # Debug Mode
    app.run(debug=True)
    # production mode 
    # p= os.environ.get('PORT')
    # p='5000' if p == None else p
    # serve(app,host='0.0.0.0', port=p)