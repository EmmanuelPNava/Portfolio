from flask import (
    Blueprint, render_template, request, redirect, url_for, current_app
)

from email.message import EmailMessage
import ssl
import smtplib

bp = Blueprint('portfolio', __name__, url_prefix='/')

@bp.route('/', methods=['GET'])
def index():
    return render_template("portfolio/index.html")

@bp.route('/mail', methods=['GET', 'POST'])
def mail():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    if request.method == 'POST':
        send_email(name, email, message)
        return render_template('portfolio/sent_mail.html')
    
    return redirect(url_for('portfolio.index'))

def send_email(name, email, message):
    mi_email = 'luisp75023@gmail.com'
    email_contraseña = current_app.config['EMAIL_PASSWORD']

    em = EmailMessage()
    em['From'] = email
    em['To'] = mi_email
    em['Subject'] = name + " / " +email
    em.set_content(message)

    contexto = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=contexto) as smtp:
        smtp.login(mi_email, email_contraseña)
        smtp.sendmail(email, mi_email, em.as_string())
