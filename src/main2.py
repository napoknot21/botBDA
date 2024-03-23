from google_sheet_handler import GoogleSheetsHandler
from discord_bot_handler import MyDiscordBot
from utils import process_team_data  # Make sure to implement this in utils.py

import asyncio

# Your Discord Bot token should be kept secure
with open("credentials/discord_token", "r") as token_file:
    discord_bot_token = token_file.read().strip()

# Initialize the Discord bot
bot = MyDiscordBot()

# Function to extract and process Google Sheets data and send notifications
async def extract_and_notify():
    # Wait until the bot is ready
    await bot.wait_until_ready()

    # Extract data from Google Sheets
    # ... (your existing code to extract Google Sheets data)
    # Make sure to pass the correct sheet name and range for each call

    # Process the data for the 'team' sheet using Pandas
    sheet_name_team = "20"
    google_sheets_handler = GoogleSheetsHandler(SPREADSHEET_ID_TEAM)
    raw_sheet_data_team = google_sheets_handler.get_sheet_data(sheet_name_team, RANGE_TEAM)
    processed_sheet_data_team = process_team_data (raw_sheet_data_team)

    # Send task notifications via Discord bot
    # Make sure to replace 'channel_name' with the actual name of the channel where notifications should be sent
    # You will need to implement the logic in MyDiscordBot.send_task_notifications() to handle processed_sheet_data_team
    await bot.send_task_notifications('channel_name', processed_sheet_data_team)

# Run the bot and start the extract_and_notify coroutine
bot.loop.create_task(extract_and_notify())
bot.run(discord_bot_token)
