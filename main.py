import disnake
import os
from disnake.ext import commands
from dotenv import load_dotenv
from os import listdir

load_dotenv()

intents = disnake.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

bot.remove_command(help)

def load_cogs():
    for filename in listdir('./func'):
        if filename.endswith('.py'):
            bot.load_extension(f'func.{filename[:-3]}')



@bot.event
async def on_ready():
    print(f'online.')



if __name__ == '__main__':
    load_cogs()
    bot.run(os.getenv("BOT_TOKEN"))