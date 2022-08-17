import nextcord
from nextcord.ext import tasks, commands
from dotenv import load_dotenv

'''
ctx.author - kto napisał
ctx.guild - jakiej uzył komendy
ctx.send() - informacja na chat
ctx.messege - informacja z czatu
'''

load_dotenv()
f = open("keys", "r")
TESTING_GUILD_ID = f.readline()
f.close()
intents = nextcord.Intents.all()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.slash_command(name="hello", description="Welcome")
async def hello(interaction: nextcord.Interaction):
    await interaction.send("Cześć! Miłej zabawy ;)")

# @bot.command()
# async def add_host(ctx, name_of_host):

# @bot.command()
# async def remove_host(ctx, name_of_host):

# @bot.command()
# async def add_guest(ctx, name_of_guest):

# @bot.command()
# async def remove_host(ctx, name_of_guest):
        


@bot.command()
async def test(ctx, arg):
    
    await ctx.send(arg)




bot.run(TESTING_GUILD_ID)
