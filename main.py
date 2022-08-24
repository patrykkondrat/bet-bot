'''
ctx.author - kto napisał
ctx.guild - jakiej uzył komendy
ctx.send() - informacja na chat
ctx.messege - informacja z czatu
'''

import nextcord
from nextcord.ext import tasks, commands
from dotenv import load_dotenv
from db_service import BetServices, TeamServices



betserv = BetServices()
teamserv = TeamServices()
load_dotenv()
with open("keys", "r") as f:
    TESTING_GUILD_ID = f.readline()

intents = nextcord.Intents.all()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.slash_command(name="hello", description="Welcome")
async def hello(interaction: nextcord.Interaction):
    await interaction.send("Hi! Have a great game ;)")

@bot.command()
async def bet(ctx, _bet):
    print("================ Someone trying to make a bet =================")
    try:
        betserv.make_bet(str(ctx.author), _bet)
        await ctx.send(f"{ctx.author} bet on {_bet}. Good luck!")
        print(f"{ctx.author} made a bet succesfully")
    except:
        await ctx.send("Something goes wrong with you bet, {ctx.author} :(")
        print(f"{str(ctx.author)} try to bet but something failed")

@bot.command()
async def sethost(ctx, host_name):
    try:
        teamserv.set_host_team(host_name)        
        await ctx.send(f"{host_name} is set as host team.")
        print(f"Host: {host_name}")
    except:
        print("Wrong host")
        await ctx.send(f"Something goes wrong")

@bot.command()
async def setguest(ctx, guest_name):
    try:
        teamserv.set_guest_team(guest_name)        
        await ctx.send(f"{guest_name} is set as host team.")
        print(f"Host: {guest_name}")
    except:
        print("Wrong host")
        await ctx.send(f"Something goes wrong")

@bot.command()
async def setwinners(ctx):
    pass
    

@bot.command()
async def showbets(ctx):
    await ctx.send(betserv.show_table(1))

@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)




bot.run(TESTING_GUILD_ID)
