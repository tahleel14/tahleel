from flask import Flask, redirect, render_template, request, url_for
from smtplib import SMTP


app = Flask(__name__)

@app.route('/')
def home():
    return(render_template('index.html'))

@app.route('/contact_me', methods=['POST'])
def contact_me():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']

        if not email and message:
            return(redirect(url_for('home')))


        with SMTP('smtp.gmail.com', 587) as server:
            try:
                msg = f"Subject: {subject}\n\n{message+f'\nEMAIL: {email}'}"
                server.starttls()
                server.login('jamesurio474@gmail.com', 'hodp urhv cbmr yqbe')
                server.sendmail('jamesurio474@gmail.com', "jimmyuricain474@gmail.com", msg)
                print("[SUCCESS] Email sent successfully!")
                return(redirect(url_for('home')))
            except Exception as e:
                print(f"[ERROR] occurred while sending email: {e}")
                return(redirect(url_for('home')))



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)
