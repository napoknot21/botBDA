from google_sheet_handler import GoogleSheetsHandler
from monitoring import monitor_sheet_for_changes
#from discord_bot_handler import BotBotHandler
from utils import *

from datetime import datetime


SPREADSHEET_ID_TEAM = "1hrIF62cG5HS0twCRoYYDZkjcJVBX-yOu4dHbCyorHag"
SPREADSHEET_ID_ZINZIN = "1EBrnd9fqqAfpvW2Tq3c2aPDH6FH3KmRS1UAZ7eIenYI"
SPREADSHEET_ID_FOOD = "1nylQH8HgAhk2McoqfGpjz0DHPrc-80-QDgXHnjL-9jE"

RANGE_TEAM = "A1:Y20"
RANGE_ZINZIN = "A1:Y20"
RANGE_FOOD = "A1:Y20"


def main () :
    

    google_sheets_handler_zinzin = GoogleSheetsHandler(SPREADSHEET_ID_ZINZIN)
    google_sheets_handler_food = GoogleSheetsHandler(SPREADSHEET_ID_FOOD)
    google_sheets_handler_team = GoogleSheetsHandler(SPREADSHEET_ID_TEAM)
    
    sheet_name_team = str(datetime.now().day)
    sheet_data_zinzin = google_sheets_handler_zinzin.get_sheet_data("", RANGE_ZINZIN)
    sheet_data_food = google_sheets_handler_food.get_sheet_data("", RANGE_FOOD)
    sheet_data_team = google_sheets_handler_team.get_sheet_data(sheet_name_team, RANGE_TEAM)

    # Team values processing
    sheet_data_team = process_team_data (sheet_data_team)
    
    
    
    


if __name__ == "__main__" : 

    main()
 