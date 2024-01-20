from google_sheet_handler import GoogleSheetsHandler

def main () :

    #SPREADSHEET_ID_TEAM = "1clVF1I8jYTEMti-flozWUTJVbC_H3-pQskDled19j-I"
    SPREADSHEET_ID_TEAM = "1hrIF62cG5HS0twCRoYYDZkjcJVBX-yOu4dHbCyorHag"
    SPREADSHEET_ID_ZINZIN = "1EBrnd9fqqAfpvW2Tq3c2aPDH6FH3KmRS1UAZ7eIenYI"
    SPREADSHEET_ID_FOOD = "1nylQH8HgAhk2McoqfGpjz0DHPrc-80-QDgXHnjL-9jE"
    
    RANGE_TEAM = "A1:Y20"
    RANGE_ZINZIN = "A1:Y20"
    RANGE_FOOD = "A1:Y20"



    google_sheets_handler = GoogleSheetsHandler(SPREADSHEET_ID_ZINZIN)
    sheet_data_zinzin = google_sheets_handler.get_sheet_data("", RANGE_ZINZIN)

    if sheet_data_zinzin :

        print(sheet_data_zinzin)
        print()


    google_sheets_handler = GoogleSheetsHandler(SPREADSHEET_ID_FOOD)
    sheet_data_food = google_sheets_handler.get_sheet_data("", RANGE_FOOD)

    if sheet_data_food :

        print(sheet_data_food)
        print()


    sheet_name_team = "20"
    google_sheets_handler = GoogleSheetsHandler(SPREADSHEET_ID_TEAM)
    sheet_data_team = google_sheets_handler.get_sheet_data(sheet_name_team, RANGE_TEAM)

    if sheet_data_team:

        print(sheet_data_team)
        print()


if __name__ == "__main__" : 

    main()
 