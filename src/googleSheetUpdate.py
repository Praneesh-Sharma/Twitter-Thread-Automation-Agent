import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

# Define the scope for Google Sheets API
SCOPES = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]

# Path to the service account JSON file
SERVICE_ACCOUNT_FILE = 'config/gen-lang-client-0877925861-fb7679841481.json'

# Authenticate using the service account credentials
creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# Use gspread to open the Google Sheet
client = gspread.authorize(creds)

# Open the Google Sheet by its title
sheet = client.open("Twitter Thread Automation Agent").sheet1

def update_google_sheet(topic, original_url, twitter_thread_url):
    """
    Updates the next available row in the Google Sheet with the given information.
    """
    # Get the current date and time
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Find the next available row
    next_row = len(sheet.get_all_values()) + 1
    
    # Update the sheet with the relevant data
    sheet.update(f"A{next_row}", [[topic, original_url, twitter_thread_url, current_datetime]])

    print(f"[INFO] Row {next_row} updated successfully with the following data:")
    print(f"Topic: {topic}\nOriginal URL: {original_url}\nTwitter Thread URL: {twitter_thread_url}\nDateTime: {current_datetime}")

