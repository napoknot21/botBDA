import os
import pandas as pd

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials 
from google_auth_oauthlib.flow import InstalledAppFlow

from googleapiclient.discovery import build 
from googleapiclient.errors import HttpError


class GoogleSheetsHandler :
    
    SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]


    def __init__ (self, spreadsheet_id, range_name) :
        
        self.spreadsheet_id = spreadsheet_id
        self.range_name = range_name
        self.credentials = self.authenticate_google_sheets()



    def authenticate_google_sheets (self) :

        credentials = None

        if os.path.exists("credentials/token.json") :

            credentials = Credentials.from_authorized_user_file ("credentials/token.json", self.SCOPES)

        if not credentials or not credentials.valid :
            
            if credentials and credentials.expired and credentials.refresh_token :
                
                credentials.refresh(Request())

            else :

                flow = InstalledAppFlow.from_client_secrets_file("credentials/google_sheets_credentials.json", self.SCOPES)
                credentials = flow.run_local_server(port=0)

            with open ("credentials/token.json", "w") as token : 

                token.write(credentials.to_json())

        return credentials



    def get_sheet_data (self) :
        
        try :

            service = build("sheets", "v4", credentials=self.credentials)
            sheet = service.spreadsheets()
            result = sheet.values().get(spreadsheetId=self.spreadsheet_id, range=self.range_name).execute()
            values = result.get("values", [])

            return values
        
        except HttpError as error:

            print(f"An error occurred : {error}")
            
            return None

