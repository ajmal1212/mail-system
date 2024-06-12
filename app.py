from flask import Flask, request, jsonify
from flask_mail import Mail, Message

app = Flask(__name__)

# Configuration for Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'ajmal1995.la@gmail.com'  # Replace with your Gmail address
app.config['MAIL_PASSWORD'] = 'your-email-password'  # Replace with your Gmail password
app.config['MAIL_DEFAULT_SENDER'] = ('Webflow Form', 'ajmal1995.la@gmail.com')

mail = Mail(app)

@app.route('/send_email', methods=['POST'])
def send_email():
    try:
        data = request.get_json()
        email = data.get('email')
        name = data.get('name')
        message_content = data.get('message')

        msg = Message('New Form Submission',
                      recipients=['ajmal1995.la@gmail.com'])  # Replace with the recipient's email if different
        msg.body = f'You have a new form submission from {name} ({email}):\n\n{message_content}'
        msg.html = f'<p>You have a new form submission from <strong>{name}</strong> ({email}):</p><p>{message_content}</p>'
        mail.send(msg)
        return jsonify({'message': 'Email sent successfully!'}), 200
    except Exception as e:
        return jsonify({'message': 'Failed to send email', 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
