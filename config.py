import os
import pyocr

BaseFolder = r""
UPLOAD_FOLDER = os.path.join(BaseFolder, "uploads")
JsonPath = os.path.join(BaseFolder, 'info.json')
form_fields = ["Name", "Invoice No.", "Invoice_Date", "Delivery_Note", "Mode_Terms_Of_Payment", "Reference_No_Date",
               "Buyer's Order No.", "Delivery Note Date", "Dispatched through", "Destination", "Quantity", "Total Amount"]

FORMFIELDSVAR = form_fields
TESTING = True
secret_key = os.urandom(24)
SESSION_TYPE = 'filesystem'
SECRET_KEY = os.urandom(24)
UPLOAD_EXTENSIONS = [".pdf"]
JSONPATH = JsonPath 
UPLOAD_PATH = UPLOAD_FOLDER
# session['FirstPageImageName'] = "{}.jpg".format(''.join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase) for i in range(14)))
MAX_CONTENT_LENGTH = 16 * 1024 * 1024
# app.config['PDFPage'] = os.path.join(UPLOAD_FOLDER, session['FirstPageImageName'])
Extracted_Text = list()




# POPPLER = r"C:\ProgramData\chocolatey\lib\poppler\tools"

# TESSER_ACT = r'C:\Program Files\Tesseract-OCR\tesseract.exe'