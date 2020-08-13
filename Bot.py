import discord, discord.utils
from discord.ext import commands
from discord.utils import get
from Functions import getdiscord, key

#TODO Implement Guild Role check
#Discord Key used to run the Bot
KEY = key.key()
#The Prefix of the Bot
PREFIX = "v!"
#The Role it gives People 
ROLE = "Hypixel Verified"

mrole = "Guild Member"
ankrole = None
# Sets Command Prefix 
client = commands.Bot(command_prefix = PREFIX)

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("https://github.com/Lulonaut/Hypixel-Verify"))
    print("Ready")

@client.event
async def on_member_join(member):
    role = get(member.guild.roles, name="Member")
    await member.add_roles(role)
    print(f"{member} was given {role}")


@client.command()
async def verify(ctx, name):
    #defines Member
    member = ctx.message.author
    #trys getting Output
    rank = None
    nickname = None
    guildrole = None
    grole = None
    Output = None
    ankrole = None

    Output = getdiscord.discordlinked(name)
    rank = getdiscord.rank(name)
    nickname = getdiscord.name(name)
    guildmember = getdiscord.guild(name)
    
    if Output == "API_ERROR":
        #Abort
        await ctx.send("There was an Error while contacting the API, please try again later or contact an Admin!")
        pass
    elif Output == "DISCORD_ERROR":
        #Abort
        await ctx.send(f"There is currently no Discord linked to the IGN: {name}. If you just updated it in game, try again in a few minutes!")
        pass
    
    if guildmember == "NOT_IN_GUILD":
        guildmember = None

    if rank == "RANK_ERROR":
        #Continue without Rank info
        await ctx.send("There was an Error while getting your rank info, maybe you are a Staff Member?")
    
    if name == "NAME_ERROR":
        #Abort
        print("There was an Error getting your Name, try again and if this keeps happening contact an Admin")
        pass


    member2 = str(member).replace("#", "")
    Output2 = str(Output).replace("#", "")

    if member2 == Output2 and ROLE != None:
        role = None
        rankrole = None
        try:
            role = discord.utils.get(ctx.guild.roles, name=ROLE)
        except:
            print(f"Error while getting Role {ROLE} ")
        try:
            rankrole = discord.utils.get(ctx.guild.roles, name=rank)
        except:
            print(f"Error while getting Role {rank} ")
        try:
            ankrole = discord.utils.get(ctx.guild.roles, name=mrole)
        except:
            print(f"Error while getting Role Guild Member ")

        try:
            await member.add_roles(role)
        except:
            print(f"Error assigning role 1 for {name}")
        try:
            await member.add_roles(rankrole)
        except:
            print(f"Error assigning Rank role for {name}")
        try:
            await member.add_roles(ankrole)
        except:
            print(f"Error assigning member role for {name}")            

        try:
            await member.edit(nick = nickname)
            await ctx.send(f"You now have the Role `{ROLE}` and i changed your Nickname to your IGN")
        except:
            await ctx.send("Sorry, i cant change your Nickname but i gave you the roles. If this keeps happening please report it!")
        

    elif Output2 == "Error":
        await ctx.send("Something went wrong, please try again! If this keeps happening the Api is probably down.")
        


    elif Output2 != member2 and ROLE != None:
        await ctx.send(f"The current Discord set on the Account `{Output}` doesnt match your discord name `{member}`. If you just changed wait a few minutes and try again.")
    
    else:
        await ctx.send("Error, maybe try again in a bit")

client.run(KEY)
