from google_sheet_handler import GoogleSheetsHandler

import discord


class MyDiscordBot (discord.Client):
    """
    name_to_discord = {
        "Aeddan" : "@.aydeunne",
        "Nolan" : "@nolanbd",
        "Bastien" : "@bastl12",
        "Joshua I" : "@josh_57",
        "Maalek" : "@maalek_banat",
        "Charly": "568881498011205656",
        "Romain" : "@rom10795",
        "Sami" : "@samil0781",
        "Matias" : "@matcy_",
        "Luc" : "@luc8359"
    }
    """
    async def on_ready(self):
        print(f'We have logged in as {self.user}')

    
    async def send_task_notifications(self, channel_name):
        # Extract data from Google Sheets
        google_sheets_handler = GoogleSheetsHandler(YOUR_SPREADSHEET_ID)
        tasks_data = google_sheets_handler.get_sheet_data(YOUR_SHEET_NAME, YOUR_RANGE)

        # Dictionary mapping names to Discord handles
        name_to_discord = {
            "Charly": "@CharlyDiscordUsername",  # Replace with actual Discord username
            # Add more mappings as needed
        }

        # Find the channel
        channel = discord.utils.get(self.get_all_channels(), name=channel_name)

        if channel:
            # Iterate over tasks and send messages
            for task in tasks_data:
                assigned_member = task[0]  # Assuming the member's name is in the first column
                task_detail = task[1]     # Assuming the task detail is in the second column
                discord_handle = name_to_discord.get(assigned_member)
                if discord_handle:
                    message = f"{discord_handle} allo de {task_detail}"
                    await channel.send(message)

    # Add more event handlers as needed

intents = discord.Intents.default()
intents.messages = True
bot = MyDiscordBot(intents=intents)
bot.run('your_bot_token')