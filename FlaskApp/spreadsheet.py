"""
Python program that takes in a spreadsheet of medical terminology and makes flash cards

author: Erica J. Lee
updated: November 6, 2017

"""
import random
# from pattern.web import *
# import string
# import urllib3
# from bs4 import BeautifulSoup
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# url = "https://docs.google.com/spreadsheets/d/1InzQ49dfqkr7XBnxoz8j7mn1Kb8JWl_NoROQH655Pnw/edit?usp=sharing"
# response = urllib3.PoolManager().request('GET', url)
# soup = BeautifulSoup(response.data.decode("utf-8"))

# print(soup)

# sheet = url.download()
# bank = plaintext(sheet).encode("UTF-8")

# use creds to create a client to interact with the Google Drive API
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Sheets API Python Quickstart'
# creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
# client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
# sheet = client.open("MedicalTerms").sheet1


# Extract and print all of the values
# list_of_hashes = sheet.get_all_records()
# print(list_of_hashes)

def get_credentials():
    """Gets valid user credentials from storage

    If nothing has been stored, or if the stored credentials are invalid,
    the Oauth2 flow is completed to obtain new credentials.

    Returns:
        Credentials, the obtained credential.

    from youtuber skaai :https://www.youtube.com/watch?v=_AXsPKOfwuI
    """

    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                    'sheets.googleapis.com-python-quickstart.json')

