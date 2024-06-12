from flask import Flask, request, jsonify
from flask_mail import Mail, Message

app = Flask(__name__)

# Configuration for the SMTP server
SMTP_SERVER = 'smtp.gmail.com'  # Replace with your SMTP server
SMTP_PORT = 587  # Replace with the appropriate port (e.g., 587 for TLS, 465 for SSL)
SMTP_USERNAME = 'maahirenterprises.a@gmail.com'  # Replace with your SMTP username
SMTP_PASSWORD = 'Ajmal1207'  # Replace with your SMTP password
USE_TLS = True  # Set to True if using TLS, False for SSL or no encryption

def send_email(subject, sender, recipients, text_body):
    msg = MIMEText(text_body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ", ".join(recipients)
    try:
        if USE_TLS:
            server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
            server.starttls()
        else:
            server = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.sendmail(sender, recipients, msg.as_string())
        server.quit()
        return True
    except Exception as e:
        print(f"Failed to send email: {e}")
        return False

@app.route('/send_email', methods=['POST'])
def send_email_route():
    data = request.json
    subject = "Registration Confirmation"
    sender = SMTP_USERNAME  # Use the configured SMTP username as sender
    recipients = [data['email']]
    text_body = f"Hello {data['name']},\n\nThank you for registering."
    success = send_email(subject, sender, recipients, text_body)
    if success:
        return jsonify({'message': 'Email sent successfully'}), 200
    else:
        return jsonify({'message': 'Failed to send email'}), 500


def send_email(subject, sender, recipients, text_body):
    msg = MIMEText(text_body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ", ".join(recipients)
    try:
        with smtplib.SMTP('localhost') as server:
            server.sendmail(sender, recipients, msg.as_string())
        return True
    except Exception as e:
        print(f"Failed to send email: {e}")
        return False

@app.route('/send_email', methods=['POST'])
def send_email_route():
    data = request.json
    subject = "Registration Confirmation"
    sender = "your-email@example.com"
    recipients = [data['email']]
    text_body = f"Hello {data['name']},\n\nThank you for registering."
    success = send_email(subject, sender, recipients, text_body)
    if success:
        return jsonify({'message': 'Email sent successfully'}), 200
    else:
        return jsonify({'message': 'Failed to send email'}), 500

# Configuration for Flask-Mail
#app.config['MAIL_SERVER'] = 'smtp.gmail.com'
#app.config['MAIL_PORT'] = 587
#app.config['MAIL_USE_TLS'] = True
#app.config['MAIL_USERNAME'] = 'ajmal1995.la@gmail.com'  # Replace with your Gmail address
#app.config['MAIL_PASSWORD'] = 'your-email-password'  # Replace with your Gmail password
#app.config['MAIL_DEFAULT_SENDER'] = ('Webflow Form', 'ajmal1995.la@gmail.com')

#mail = Mail(app)

#@app.route('/send_email', methods=['POST'])
#def send_email():
#    try:
#        data = request.get_json()
#        email = data.get('email')
#        name = data.get('name')
#        message_content = data.get('message')

#        msg = Message('New Form Submission',
#                      recipients=['ajmal1995.la@gmail.com'])  # Replace with the recipient's email if different
#        msg.body = f'You have a new form submission from {name} ({email}):\n\n{message_content}'
#        msg.html = f'<p>You have a new form submission from <strong>{name}</strong> ({email}):</p><p>{message_content}</p>'
#        mail.send(msg)
#        return jsonify({'message': 'Email sent successfully!'}), 200
#    except Exception as e:
#        return jsonify({'message': 'Failed to send email', 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
