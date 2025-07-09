input_directory = "C:/codes/clear-cleartrip/code/data/raw_input/"
file = "C:/codes/clear-cleartrip/code/data/pdf/"
pdf_directory = "C:/codes/clear-cleartrip/code/data/pdf/"
xlsx_directory = "C:/codes/clear-cleartrip/code/data/annexure/"
raw_annexure = "C:/codes/clear-cleartrip/code/data/raw_annexure/"
archive_raw_input = "C:/codes/clear-cleartrip/code/data/archive_raw_input/"
archive_raw_annexure = "C:/codes/clear-cleartrip/code/data/archive_raw_annexure/"
output = "C:/codes/clear-cleartrip/code/data/output/"
final_output = "C:/codes/clear-cleartrip/code/data/final_output/"


api_url = "https://api-sandbox.clear.in/einv/v2/eInvoice/generate"
# api_ewb = 'https://api.clear.in/einv/v3/ewaybill/generate'
get_buyer = 'https://gst.cleartax.in/api/v0.2/taxable_entities/6c1a6a2d-9488-4604-a588-68a555995ef0/gstin_verification?gstin='
api_pdf = 'https://api-sandbox.clear.in/einv/v2/eInvoice/download?'

headToken_gst = "1.ff8b252f-2da2-4c00-a48e-01e6f2df85b7_6fe77427819250eed569accb0cec47b468bdc9f5d819bd684e4b95a3426df0ab"
headToken = '1.81b4efea-1c92-4663-809e-a223edc1b958_a00df27d9a681500412ab45a14ce33a05051eb887d04b70e86e94f5214caf74e'


api_key = '6657f9e689ecf5d7c788495b3cc3d450'



# Email configuration
smtp_server = "smtp.office365.com"  # Replace with your SMTP server (e.g., smtp.gmail.com)
port = 587                        # Port number (587 for TLS, 465 for SSL)
sender_email = "rohan.d@cloudare.in"  # Your email address
password = "Payal@0809"              # Your email password
receiver_email = "rohan.d@cloudare.in" #"sailesh@cloudare.in" # Recipient email address
cc_emails = ["hotel.accounts@cleartrip.com"]  # List of CC recipients

