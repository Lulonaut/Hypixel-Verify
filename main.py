import discord, asyncio, discord.utils
from discord.ext import commands
from discord.utils import get
from Functions import getdiscord, key



KEY = key.key()
PREFIX = "-"
#assigned later
ROLE = None

# Sets Command Prefix and removes existing #help command
client = commands.Bot(command_prefix = PREFIX)
client.remove_command("help")

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game(f"{PREFIX}help"))
    print("Ready")

@client.command(aliases=["start", "setup"])
@commands.has_permissions(manage_messages=True)
async def init(ctx, role):
    global ROLE
    ROLE = role
    await ctx.send(f"Setup Complete. The Bot will now give the Role `{ROLE}` to everyone that verifys. Please make sure this Role exists!")



@client.command(aliases=["v"])
async def verify(ctx, name):
    #defines Member
    member = ctx.message.author
    #trys getting Output
    try:
        Output = getdiscord.data(name)

    except:
        await ctx.send("Error with api")

    member2 = str(member).replace("#", "")
    Output2 = str(Output).replace("#", "")

    if member2 == Output2 and ROLE != None:
        role = discord.utils.get(ctx.guild.roles, name=ROLE)
        await member.add_roles(role)
        await ctx.send(f"You now have the Role `{ROLE}`")

    elif Output2 == "Error":
        await ctx.send("Something went wrong, please try again! If this keeps happening the Api is probably down.")
        


    elif Output2 != member2 and ROLE != None:
        await ctx.send(f"The current Discord set on the Account `{Output}` doesnt match your discord name `{member}`. If you just changed wait a few minutes and try again.")
        
    else:
        await ctx.send(f"Please setup the Bot First with `{PREFIX}setup (role)` or make sure your role exists and can be assigned! ")


    

@client.command()
@commands.has_permissions(manage_messages=True)
async def prefix(ctx, prefix):
    global PREFIX
    PREFIX = prefix
    client.command_prefix = PREFIX
    await client.change_presence(status=discord.Status.online, activity=discord.Game(f"{PREFIX}help"))
    await ctx.send(f"The new Prefix is now {PREFIX}")

client.run(KEY)
