from flask import Flask, render_template, jsonify
from utils.detector import detect_motion
import datetime
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

# Email configuration
EMAIL_ADDRESS = 'youremail@example.com'     # Replace with your email
EMAIL_PASSWORD = 'yourpassword'             # Replace with your email password
RECIPIENT_EMAIL = 'recipient@example.com'   # Replace with recipient email

def send_email_alert():
    msg = EmailMessage()
    msg['Subject'] = 'Intruder Alert!'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = RECIPIENT_EMAIL
    msg.set_content('An intruder has been detected by the Centralized Detection System.')

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
        print("Email sent successfully.")
    except Exception as e:
        print("Error sending email:", e)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check')
def check_intrusion():
    status = detect_motion()
    if status == "Intruder":
        with open("alerts/alert_log.txt", "a") as log:
            log.write(f"{datetime.datetime.now()} - Intrusion detected!\n")
        send_email_alert()
    return jsonify({'status': status})

if __name__ == '__main__':
    app.run(debug=True)