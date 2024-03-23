"""import discord
import asyncio
import os

intents = discord.Intents.default()
intents.messages = True

client = discord.Client(intents=intents)

async def send_regular_message(channel_id):
    await client.wait_until_ready()
    user_id = '568881498011205656'  # Your user ID
    channel = client.get_channel(channel_id)  # Pass channel_id as integer
    if channel:
        while not client.is_closed():
            await channel.send(f'<@{user_id}> Hello! This is a regular message.')
            await asyncio.sleep(60)  # Wait for 60 seconds

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    channel_id = 1198243914717597857  # Your channel ID as an integer
    client.loop.create_task(send_regular_message(channel_id))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send(f'<@{message.author.id}> hello !')  # Reply to the user who sent the message

with open("credentials/discord_token", "r") as token_file:
    token = token_file.read().strip()

client.run(token)
"""
import discord
import asyncio
import os

class MyDiscordBot(discord.Client):

    def __init__(self, token_path, intents, channel_mapping, user_mapping):
    
        super().__init__(intents=intents)
        self.token_path = token_path
        self.channel_mapping = channel_mapping  # Mapping of channel names to IDs
        self.user_mapping = user_mapping        # Mapping of user names to IDs

    
    def send_task_notification(self, channel_name, task_info):
        """Send a formatted task notification to a specified channel."""
        channel_id = self.channel_mapping.get(channel_name)
        
        if channel_id:

            channel = self.get_channel(channel_id)
            
            if channel:
                
                member_id = self.user_mapping.get(task_info['name'])
                
                if member_id:
                    
                    message = f"<@{member_id}> has a task: {task_info['task']} in {task_info['building']} room {task_info['room_number']}"
                    await channel.send(message)

    
    
    async def on_ready(self):
        
        print(f'Logged in as {self.user}')

    
    
    async def start_bot(self):
        """Load the bot token and run the bot."""
        with open(self.token_path, "r") as token_file:
            token = token_file.read().strip()
        self.run(token)

# Example usage:

# Define your intents
intents = discord.Intents.default()
intents.messages = True

# Mapping channel names to their IDs
channel_mapping = {
    "general": 123456789012345678  # Replace with actual channel ID
    # ... other channel mappings
}

# Mapping user names to their Discord IDs
user_mapping = {
    "Charly": 568881498011205656,  # Replace with actual Discord ID
    # ... other user mappings
}

# Initialize the bot
my_bot = MyDiscordBot("credentials/discord_token", intents, channel_mapping, user_mapping)

# Example task information
task_info_example = {
    "name": "Charly",
    "task": "deliver food",
    "building": "Main",
    "room_number": "101"
}

# Start the bot and send a notification (you would typically call this from another part of your code)
my_bot.start_bot()

# To send a notification, ensure the bot is ready and then call:
# await my_bot.send_task_notification("general", task_info_example)
