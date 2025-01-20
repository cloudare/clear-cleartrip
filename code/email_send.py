import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

file = "C:/codes/cleartrip/code/pdf/"

# Email configuration
smtp_server = "smtp.office365.com"  # Replace with your SMTP server (e.g., smtp.gmail.com)
port = 587                        # Port number (587 for TLS, 465 for SSL)
sender_email = "rohan.d@cloudare.in"  # Your email address
password = ""              # Your email password
receiver_email = "sailesh@cloudare.in" #"sailesh@cloudare.in" # Recipient email address
cc_emails = ["rohan.d@cloudare.in", "rohandutta3200@gmail.com"]  # List of CC recipients

# Email content
subject = "Test Email"
body = f"""Hello {receiver_email},

This is a test email sent from Python!

{sender_email}
"""

# Create the email
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Cc"] = ", ".join(cc_emails)
message["Subject"] = subject

# Attach the email body
message.attach(MIMEText(body, "plain"))

# File to attach
file_path = "C:/codes/cleartrip/code/Mail_sample.pdf"  # Path to the file on your system
custom_file_name = "cleartrip.pdf"  # Desired file name for the recipient
# pdf_filename = f"{file}"  # Replace with your PDF file path

# Combine all recipients (To + CC)
all_recipients = [receiver_email] + cc_emails

try:
    with open(file_path, "rb") as file:
        # Create a MIMEBase object
        attachment = MIMEBase("application", "octet-stream")
        attachment.set_payload(file.read())
        
    # Encode the file payload in Base64
    encoders.encode_base64(attachment)

    # Add header to set custom file name
    attachment.add_header(
        "Content-Disposition",
        f"attachment; filename={custom_file_name}",
    )

    # Attach the file to the message
    message.attach(attachment)

except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
    exit()

try:
    # Connect to SMTP server
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls()  # Upgrade to secure connection
        server.login(sender_email, password)  # Login to your email account
        server.sendmail(sender_email, all_recipients, message.as_string())  # Send email
        print("Email sent successfully!")
except Exception as e:
    print(f"Error occurred: {e}")
