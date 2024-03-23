from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_responses

load_dotenv()
TOKEN: Final[str] = os.getenv("DISCORD_TOKEN")
print(TOKEN)

intents : Intents = Intents.default()
intents.message_content = True
client : Client = Client(intents=intents)


async def send_message (message: Message, user_message: str) -> None:

    if not user_message:
        print('(Message was empty because intents were not enable probably)')
        return

    if is_private := user_message[0] == '?':
        user_message = user_message[1:]
    
    try :

        responses: str = get_responses(user_message)
        await message.author.send(responses) if is_private else await message.channel.send(responses)
    
    except Exception as e :
        print(e)


@client.event
async def on_ready ()  -> None :
    print(f'{client.user} is now running!')


@client.event
async def on_message (message: Message) -> None :
    if message.author == client.user:
        return

    username : str = str(message.author)
    user_message : str = message.content
    channel: str = str(message.channel)

    print(f'[{channel}] {username}: {user_message}')
    await send_message(message, user_message)


def main () -> None :
    client.run(TOKEN)

if __name__ == '__main__':
    main()



















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
    channel_id = 1198209834256973834  # Your channel ID as an integer
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