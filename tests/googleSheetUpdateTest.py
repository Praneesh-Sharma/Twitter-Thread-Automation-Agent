#testing script for updating the google sheet
import gspread
from google.oauth2.service_account import Credentials

# Define the scope for Google Sheets API
SCOPES = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]

# Path to the service account JSON file
SERVICE_ACCOUNT_FILE = 'config/reverberant-kit-427620-b4-09e5ab7eef10.json'

# Authenticate using the service account credentials
creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# Use gspread to open the Google Sheet
client = gspread.authorize(creds)

# Open the Google Sheet by its title
sheet = client.open("Twitter Thread Automation Agent").sheet1

# Example: Update a cell in the sheet
sheet.update(values=[['Hello, world!']], range_name='A2')