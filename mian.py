import nextcord
from nextcord.ext import commands

import os
from dotenv import load_dotenv

load_dotenv()

TESTING_GUILD_ID = "MTAwNjYzMDUxNzUzOTYxMDc0Nw.GpLaw6.t5eW2ia8ZLQYDo0Yg1yixrF2EvaLuquKJ_ChYo"

bot = commands.Bot()

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.slash_command(description="My first slash command")
async def hello(interaction: nextcord.Interaction):
    await interaction.send("Hello!")

bot.run(TESTING_GUILD_ID)
