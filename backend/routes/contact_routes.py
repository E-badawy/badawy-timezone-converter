from flask import Blueprint, request, jsonify
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

contact_bp = Blueprint('contact', __name__, url_prefix='/api')

# Email configuration
SENDER_EMAIL = 'officialbadawy@gmail.com'
SENDER_PASSWORD = 'your_app_password_here'  # Use Gmail App Password
RECIPIENT_EMAIL = 'officialbadawy@gmail.com'

@contact_bp.route('/contact', methods=['POST'])
def send_contact_message():
    """Handle contact form submissions"""
    try:
        data = request.json
        
        # Validate required fields
        required_fields = ['name', 'email', 'subject', 'message']
        if not all(field in data for field in required_fields):
            return jsonify({'error': 'Missing required fields'}), 400
        
        name = data['name'].strip()
        email = data['email'].strip()
        subject = data['subject'].strip()
        message = data['message'].strip()
        
        # Validate email format
        if '@' not in email or '.' not in email:
            return jsonify({'error': 'Invalid email address'}), 400
        
        # Create email message
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = RECIPIENT_EMAIL
        msg['Subject'] = f"New Contact Form: {subject}"
        
        # Email body
        body = f"""
        New message from CIGMA Timezone Converter Contact Form
        
        Name: {name}
        Email: {email}
        Subject: {subject}
        
        Message:
        {message}
        
        ---
        This is an automated message from CIGMA Timezone Converter
        """
        
        msg.attach(MIMEText(body, 'plain'))
        
        try:
            # Send email via Gmail SMTP
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.send_message(msg)
            server.quit()
            
            return jsonify({
                'success': True,
                'message': 'Message sent successfully!'
            }), 200
            
        except smtplib.SMTPAuthenticationError:
            # If email sending fails, log it but don't block the user
            print(f"Email auth failed - Message from {name} ({email}): {message}")
            return jsonify({
                'success': True,
                'message': 'Message received! We will contact you shortly.'
            }), 200
        except Exception as e:
            print(f"Email error: {str(e)}")
            # Still return success to user, but log the error
            return jsonify({
                'success': True,
                'message': 'Message received! We will contact you shortly.'
            }), 200
            
    except Exception as e:
        return jsonify({'error': f'Server error: {str(e)}'}), 500
