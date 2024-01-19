from google_sheet_handler import GoogleSheetsHandler

def main () :

    SPREADSHEET_ID = "1hrIF62cG5HS0twCRoYYDZkjcJVBX-yOu4dHbCyorHag"
    RANGE = "A1:Y20"

    """
    SPREADSHEET_ID = "1hrIF62cG5HS0twCRoYYDZkjcJVBX-yOu4dHbCyorHag"
    #SPREADSHEET_ID = "1clVF1I8jYTEMti-flozWUTJVbC_H3-pQskDled19j-I"

    #RANGE = "A1:B9"
    RANGE = "A1:Y20"
    """

    google_sheets_handler = GoogleSheetsHandler(SPREADSHEET_ID, RANGE)
    sheet_data = google_sheets_handler.get_sheet_data()

    if sheet_data :

        print(sheet_data)


if __name__ == "__main__" : 

    main()
 