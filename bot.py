from config import token
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if "https://" in message.content:
        await message.channel.send("Sorry, messages containing links are not allowed here.")
        # WARNING!!! This part of the code REQUIRES 'Manage Messages' PERMISSION IN THE SERVER. PLEASE COMMENT THIS PART IF NOT NECESSARY.
        try:
            await message.delete()
        except discord.Forbidden:
            print(f"Error: Bot does not have permission to delete messages in {message.channel.name}")
        except discord.HTTPException as e:
            print(f"Error deleting message: {e}")
        return

    await message.channel.send(message.content)

client.run(TOKEN)
