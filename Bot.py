import re
import time
from Functions.getdiscord import guild
import discord
import discord.utils
from discord.ext import commands
from discord.utils import get
from Functions import getdiscord, key
import asyncio

# Discord Key used to run the Bot
KEY = key.key()
# The Prefix of the Bot
PREFIX = "v!"
# The Role it gives People
ROLE = "Hypixel Verified"
# Role it gives new people that join
AUTOROLE = "Member"

mrole = "Guild Member"
ankrole = None
# Sets Command Prefix
client = commands.Bot(command_prefix=PREFIX)


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("https://github.com/Lulonaut/Hypixel-Verify"))
    print("Ready")


@client.event
async def on_member_join(member):
    role = get(member.guild.roles, name=AUTOROLE)
    await member.add_roles(role)
    print(f"{member} was given {role}")


@client.command()
async def verify(ctx, name):
    print("kk")
    # defines Variables to avoid errors later
    member = ctx.message.author

    rank = None
    nickname = None
    guildrole = None
    grole = None
    Output = None
    ankrole = None

    # Get info from API

    Output = getdiscord.discordlinked(name)
    rank = getdiscord.rank(name)
    nickname = getdiscord.name(name)
    guildmember = getdiscord.guild(name)

    # Error handling

    if Output == "API_ERROR":
        # Abort
        await ctx.send("There was an Error while contacting the API, please try again later or contact an Admin!")
        return
    elif Output == "DISCORD_ERROR":
        # Abort
        await ctx.send(f"There is currently no Discord linked to the IGN: {name}. If you just updated it in game, try again in a few minutes! ")
        return

    if guildmember == "NOT_IN_GUILD":
        guildmember = None

    if rank == "RANK_ERROR":
        # Continue without Rank info
        await ctx.send("There was an Error while getting your rank info, maybe you are a Staff Member?")

    if name == "NAME_ERROR":
        # Abort
        print("There was an Error getting your Name, try again and if this keeps happening contact an Admin")
        return

    # Makes Strings comparable to check if API matches with Discord Tag
    member2 = str(member).replace("#", "")
    Output2 = str(Output).replace("#", "")

    # When compared adds Roles and changes Nickname
    if member2 == Output2 and ROLE != None:
        role = None
        rankrole = None

        # defines the roles
        try:
            role = discord.utils.get(ctx.guild.roles, name=ROLE)
            annPing = discord.utils.get(
                ctx.guild.roles, name="Announcement Ping")
            evePing = discord.utils.get(ctx.guild.roles, name="Event Ping")
        except:
            print(f"Error while getting Role {ROLE} or pings")
        try:
            rankrole = discord.utils.get(ctx.guild.roles, name=rank)
        except:
            print(f"Error while getting Role {rank} ")
        try:
            ankrole = discord.utils.get(ctx.guild.roles, name=mrole)
        except:
            print(f"Error while getting Role Guild Member ")
        # Adds the roles
        try:
            await member.add_roles(role)
            await member.add_roles(annPing)
            await member.add_roles(evePing)
        except:
            print(f"Error assigning role 1 for {name}")
        try:
            await member.add_roles(rankrole)
        except:
            print(f"Error assigning Rank role for {name}")
        try:
            if guildmember == "Gmember":
                await member.add_roles(ankrole)
        except:
            print(f"Error assigning member role for {name}")

        # Changes Nickname
        try:
            await member.edit(nick=nickname)
            await ctx.send(f"You now have the Role `{ROLE}` and i changed your Nickname to your IGN")
        except:
            await ctx.send("Sorry, i cant change your Nickname but i gave you the roles. If this keeps happening please report it!")

    # Error, idk if this is ever used
    elif Output2 == "Error":
        await ctx.send("Something went wrong, please try again! If this keeps happening the Api is probably down.")

    # Shows the Error when it doesnt match
    elif Output2 != member2 and ROLE != None:
        await ctx.send(f"The current Discord set on the Account `{Output}` doesnt match your discord name `{member}`. If you just changed it in game wait a few minutes and try again.")

    else:
        await ctx.send("Error, maybe try again in a bit")


# Setup part, NOT COMPLETED
@client.event
async def on_message(message):

    if message.content.startswith('v!setup'):
        # return as its not finished yet!
        return
        channel = message.channel
        # Timout for answering
        default_timeout = int(420)

        # Removes text of Permission id to make it comparable
        s = message.author.permissions_in(message.channel)
        s = str(s)
        s = re.sub("\D", "", s)
        s = int(s)

        # Cheks if user has "manage_roles" permision

        if s < 268435456:
            await channel.send("Sorry you dont have the permission to do that. Ask an Admin to do it!")
            return

        # Check to see if message is from the same user and in the same channel as the original one
        def check(m):
            if c == m.content:
                return m.channel == message.channel and m.author == message.author
            elif c == None:

                return m.channel == message.channel and m.author == message.author

        # Actual Setup
        start = await channel.send('initializing Setup... :upside_down:')
        time.sleep(1.5)

        author = str(message.author.mention)
        channelMention = str(message.channel.mention)
        default_timeout = str(default_timeout)
        embed = discord.Embed()
        embed.set_author(name="Lulonaut", url="https://github.com/Lulonaut/")
        embed.add_field(name="Basic Info", value="\n**A few things before we start:\n1.** Only " + author + " can respond to this message in the channel " + channelMention + " , Everything else will be ignored\n**2.** The Timeout for answering a message is " + default_timeout +
                        " seconds unless noted otherwise\n**3.** All info that you enter here is stored on a server and is only changed for this Discord Server\n**4.** Info wont be deleted if you kick or ban the Bot, however you can rerun the Setup at any time.\n\nType **start** to continue with the setup", inline=False)
        embed.set_footer(text=":)")
        await channel.send(embed=embed)
        time.sleep(1)
        # First "start" Question
        try:
            c = "start"
            msg = await client.wait_for('message', timeout=1000, check=check)

        except asyncio.TimeoutError:
            await channel.send("Sorry you took to long to respond! Try again")
            return

        embed = discord.Embed()
        embed.set_author(name="Lulonaut", url="https://github.com/Lulonaut/")
        embed.add_field(name="Verify Role", value="Okay we can start!\nPlease enter the Role people should get after verifying! This is required for minimal Operation and you can stop after this if you want!", inline=False)
        embed.add_field(name="How to respond",
                        value="Please respond with the exact Role Name and make sure it exists!\nI would suggest copying it from the Role Menu", inline=False)
        embed.set_footer(text=":)")
        await channel.send(embed=embed)
        try:
            default_timeout = int(default_timeout)
            c = "LOL"
            msg = await client.wait_for('message', timeout=default_timeout, check=check)

        except asyncio.TimeoutError:
            await channel.send("Sorry you took to long to respond! Try again")
            return

        return

    await client.process_commands(message)

client.run(KEY)
