import os
import re
import time
import discord
import discord.utils
import asyncio
import traceback
import time
import EDITME as tkn
from discord.ext import commands
from discord.utils import get
from Functions import getdiscord, requesthandler, logmsg, msgstorage, Bots


intents = discord.Intents(members=True,presences=True, messages=True, guilds = True)
client = commands.Bot(command_prefix='v!', intents=intents)

# Discord Token used to run the Bot
try:
    KEY = tkn.TOKEN
except:
    print("Looks like there is no Token in the File, please add one (dont forget to save) and try again!")
    ex = input("Press any key to close")
    if ex:
        exit()

# The Role it gives People
ROLE = "Hypixel Verified"
# Role it gives new people that join
AUTOROLE = "Member"

mrole = "Guild Member"
ankrole = None


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("https://github.com/Lulonaut/Hypixel-Verify"))
    logmsg.logmsg("[INFO] NEW SESSION\n")


@client.event
async def on_member_join(member):
    role = get(member.guild.roles, name=AUTOROLE)
    await member.add_roles(role)
    logmsg.logmsg(f"[NEW MEMBER] {member} was given {role}")


@client.command(aliases=["git"])
async def github(ctx):
    await ctx.send("This Bot is open-source and you can take a look at it here: https://github.com/Lulonaut/Hypixel-Verify ")


@client.command()
async def verify(ctx, name):
    # defines Variables to avoid errors later
    member = ctx.message.author

    rank = None
    nickname = None
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
            logmsg.logmsg(
                f"[VERIFY COMMAND] Error while getting Role {ROLE} or pings")
        try:
            rankrole = discord.utils.get(ctx.guild.roles, name=rank)
        except:
            logmsg.logmsg(f"[VERIFY COMMAND] Error while getting Role {rank} ")
        try:
            ankrole = discord.utils.get(ctx.guild.roles, name=mrole)
        except:
            logmsg.logmsg(
                f"[VERIFY COMMAND] Error while getting Role Guild Member ")
        # Adds the roles
        try:
            await member.add_roles(role)
            await member.add_roles(annPing)
            await member.add_roles(evePing)
        except:
            logmsg.logmsg(
                f"[VERIFY COMMAND] Error assigning role 1 for {name}")
        try:
            await member.add_roles(rankrole)
        except:
            logmsg.logmsg(
                f"[VERIFY COMMAND] Error assigning Rank role for {name}")
        try:
            if guildmember == "Gmember":
                await member.add_roles(ankrole)
        except:
            logmsg.logmsg(
                f"[VERIFY COMMAND] Error assigning member role for {name}")

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


@client.command()
async def tryhard(ctx):
    # return
    # Tryhard Role in the Discord
    tryhardrole = discord.utils.get(ctx.guild.roles, name="TryHard")
    # The ticket Channel where they can open tickets
    TICKET_CHANNEL = client.get_channel(737011590729039954)

    # Message that gets deleted after its done
    wait = await ctx.send("Please wait a bit while the Bot checks your stats!")
    # Requests Output for the users Nickname, which should be their IGN set in v!verify
    out = None
    try:
        out = requesthandler.tryhard(ctx.message.author.display_name)
    except:
        await ctx.send("Looks like the API is down or some other Error occured :(")

    await wait.delete()
    # assigns Roles for the specific Outputs
    if out == "a":
        try:
            await ctx.message.author.add_roles(tryhardrole)
        except:
            logmsg.logmsg(
                f"f[TRYHARD COMMAND] Error assigning Role to {ctx.message.author.display_name}")
            await ctx.send("I cant give you the Tryhard Role, probably because you have higher Permissions than me. If you dont have higher perms and this Issue keeps coming, please open a ticket or contact a staff Member!")
            return

        await ctx.send(f"Good News! You meet the requirements (Skill Average over 30). I gave you the Discord role. To recive the Role in game please open a Ticket")
    elif out == "b":
        try:
            await ctx.message.author.add_roles(tryhardrole)
        except:
            logmsg.logmsg(
                f"f[TRYHARD COMMAND] Error assigning Role to {ctx.message.author.display_name}")
            await ctx.send("I cant give you the Tryhard Role, probably because you have higher Permissions than me. If you dont have higher perms and this Issue keeps coming, please open a ticket or contact a staff Member!")
            return

        await ctx.send(f"Good News! You meet the requirements (Skill Average over 25 and two Slayers at lvl7). I gave you the Discord role. To recive the Role in game please open a Ticket")

    elif out == "c":
        await ctx.send(f"Sorry, it looks you are not meeting the requirements. If you are sure that you meet them please make sure your Skill API is turned on and try again in a few minutes. If you still have Issues create a ticket  or contact a staff Member")

    elif out == "d":
        await ctx.send("There was an Error while getting your Profiles, please make sure your Discord Nickname is your IGN and you played Skyblock before. ")
        return

    elif out == "e":
        await ctx.send("Looks like the API is down, please try again in a few minutes.")

    elif out == None:
        await ctx.send("This shouldnt happen, please be so kind and report it :D")

    else:
        await ctx.send("This shouldnt happen, please be so kind and report it :D")

# Setup part, NOT COMPLETED


@client.event
async def on_message(message):

    if message.content.startswith('v!setup'):
        # return as its not finished yet!
        return
        channel = message.channel
        # Timout for answering
        default_timeout = int(1000)

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
        await channel.send('initializing Setup... :upside_down:')
        time.sleep(1.5)

        # first embed for the start question
        author = str(message.author.mention)
        channelMention = str(message.channel.mention)
        default_timeout = str(default_timeout)
        embed = discord.Embed()
        embed.add_field(name="Basic Info", value="\n**A few things before we start:\n1.** Only " + author + " can respond to this message in the channel " + channelMention + " , Everything else will be ignored\n**2.** The Timeout for answering a message is " + default_timeout +
                        " seconds unless noted otherwise\n**3.** All info that you enter here is stored on a server and is only changed for this Discord Server\n**4.** Info wont be deleted if you kick or ban the Bot, however you can rerun the Setup at any time.\n\nType **start** to continue with the setup", inline=False)
        embed.set_footer(text=f"Coded by Lulonaut",
                         icon_url="https://avatars2.githubusercontent.com/u/67191924?s=400&u=442455cc574e59445631175d00733d055991a336&v=4")
        await channel.send(embed=embed)
        time.sleep(1)
        # First "start" Question
        try:
            c = "start"
            msg = await client.wait_for('message', timeout=1000, check=check)

        except asyncio.TimeoutError:
            await channel.send("Sorry you took to long to respond! Try again")
            return
        # embed for the verify Role Question
        embed = discord.Embed()
        embed.add_field(name="Verify Role", value="Okay we can start!\nPlease enter the Role people should get after verifying. This is required for minimal Operation and you can stop after this if you want.", inline=False)
        embed.add_field(name="How to respond",
                        value="Please respond with the exact Role Name and make sure it exists!\nI would suggest copying it from the Role Menu", inline=False)
        embed.set_footer(text=f"Coded by Lulonaut",
                         icon_url="https://avatars2.githubusercontent.com/u/67191924?s=400&u=442455cc574e59445631175d00733d055991a336&v=4")
        startEmbed = await channel.send(embed=embed)
        # verify role question
        try:
            default_timeout = int(default_timeout)
            c = None
            msg = await client.wait_for('message', timeout=default_timeout, check=check)

            # TODO First variable to be saved
            toSaveVROLE = msg.content
            logmsg.logmsg(toSaveVROLE)
            client.delete_message(startEmbed)
            await channel.send("Input saved!")

        except asyncio.TimeoutError:
            await channel.send("Sorry you took to long to respond! Try again")
            return
        # rank role embed
        embed = discord.Embed()
        embed.add_field(
            name="Rank Role", value="The Bot can check the Rank a player has and give them the corresponding role. Do you want this enabled?", inline=True)
        embed.add_field(name="How to Respond", value="Simply respond with ""yes"" or ""no"", or if you dont want anything else after this (Check Github README for info) type ""stop"" to end the setup now.\nWhen responding with yes please make sure the following Roles exist: 1. VIP 2. VIP+ 3. MVP 4. MVP+ 5. MVP++\nIf they dont exist the feature wont work, but it wont break anything else.", inline=True)
        await channel.send(embed=embed)

        return

    await client.process_commands(message)


@client.event
async def on_message(message):
    BotList = Bots.getBots()
    if str(message.author) in BotList:
        logmsg.logmsg(
            f"[NEW MESSAGE] Not counting message from {message.author} because its a Bot")
        return

    if str(message.channel).startswith("bz_"):
        logmsg.logmsg(
            f"[NEW MESSAGE] Not counting message from {message.author} because it's in Channel {message.channel} which is a Bazcal Channel")
        await client.process_commands(message)
        return

    try:
        msgstorage.Handle(str(message.author.id), "add")
        logmsg.logmsg(f"[NEW MESSAGE] added one message for {message.author}")
    except:
        logmsg.logmsg(
            f"[NEW MESSAGE] Error while adding message for {message.author}")
        traceback.print_exc()
    await client.process_commands(message)


@client.event
async def on_message_delete(message):
    try:
        msgstorage.Handle(str(message.author.id), "remove")
        logmsg.logmsg(
            f"[MESSAGE DELETED] removed one message for {message.author}")
    except:
        logmsg.logmsg(
            f"[MESSAGE DELETED] Error while removing message for {message.author}")
    await client.process_commands(message)


@client.command()
async def checkmsg(ctx):
    def getmsgcount():
        output = []
        messages = msgstorage.loadfromjson()
        messages_sorted = sorted(messages, key=messages.get, reverse=True)
        for i in range(10):
            try:
                currp = str(messages_sorted[i])
                currpp = messages[currp]
                if currp == "Placeholder":
                    print("PLACEHOLDER DETECTED")
                    return output
                currp = int(currp)
                output.append(
                    f"<@!{currp}> has {currpp} Messages and is Place {i+1}")

            except IndexError:
                print("Index error")

            except:
                traceback.print_exc()
                print("some other error")

        return output

    try:
        output = getmsgcount()
    except:
        finout = "Error"
        await ctx.send("error :(")
    try:
        finout = f"{output[0]}\n{output[1]}\n{output[2]}\n{output[3]}\n{output[4]}\n{output[5]}\n{output[6]}\n{output[7]}\n{output[8]}\n{output[9]}\n"
    except:
        try:
            finout = f"{output[0]}\n{output[1]}\n{output[2]}"
        except:
            finout = "Error"
            await ctx.send("Can't get usable stats, please make sure at least 3 People typed since the Bot was here.")

    embed = discord.Embed(title="Current Message Stats")
    embed.add_field(name="stats", value=finout, inline=True)
    #embed.add_field(name="reset", value="To reset these values type v!clearmsg", inline=False)
    await ctx.send(embed=embed)

try:
    client.run(KEY)
except:
    print(
        f"The Bot got the following Token: {KEY} but it looks like its invalid! Please add a valid one and try again.")
    traceback.print_exc()
