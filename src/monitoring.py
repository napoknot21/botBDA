import asyncio

async def monitor_sheet_for_changes(spreadsheet_id, range_name, last_data, process_change_function, google_sheets_handler):
    
    while True:
        # Retrieve the current data from the sheet
        current_data = google_sheets_handler.get_sheet_data("", range_name)

        # If last_data is not empty, compare and find new entries
        if last_data:

            new_rows = [row for row in current_data if row not in last_data]
            
            if new_rows:
                
                await process_change_function(new_rows)

        # Update the last known data
        last_data[:] = current_data

        # Wait for 5 minutes before the next check
        await asyncio.sleep(300)



async def process_new_rows(new_rows):

    for row in new_rows:
    
        print(f"New row detected: {row}")