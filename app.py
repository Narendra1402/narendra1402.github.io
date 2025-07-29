from flask import Flask, request, jsonify
import smtplib
from email.message import EmailMessage
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow requests from frontend

# Email Configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_SENDER = "narendra3750@gmail.com"
EMAIL_PASSWORD = "sywv gftf gewt pnxz"  # Use App Password if Gmail

@app.route("/send", methods=["POST"])
def send_email():
    data = request.get_json()

    msg = EmailMessage()
    msg["Subject"] = f"Contact Form: {data.get('visit')}"
    msg["From"] = EMAIL_SENDER
    msg["To"] = data.get("email")  # you can change this to your email to receive all

    body = f"""
    You received a new contact form submission:

    Name: {data.get('fullname')}
    Email: {data.get('email')}
    Visit Time: {data.get('meeting')}
    Message: {data.get('notes')}
    """

    msg.set_content(body)

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.send_message(msg)
        return jsonify({"message": "Email sent successfully"}), 200
    except Exception as e:
        print("Error sending email:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
