# Hypixel-Verify
Verifys Players from the Hypixel Network in Minecraft and gives them a role on your discord server!

# Commands


v!verify (Username) // Checks if they connected their discord and adds a role if they did

# Getting the Bot running

### Info
You can use my Bot by inviting it [here](https://discord.com/oauth2/authorize?client_id=734124502027599925&permissions=402738176&scope=bot)
However if you do not trust me or simply want to host it on your own, follow the instructions below. Please note that your PC has to be online 24/7 if you want to host it on your own. So i would consider hosting it on a dedicated Server or somewhere else.


### Python Version

The Python version 3.6 or newer is required, because the Bot uses so called "f-Strings" which were introduced in this Version.

### Packages
After you installed the correct version you will need to install some packages which are needed to run the Bot. These are created by others and i take no credit for them.

The packages beeing used are:


discord - [discord.py](https://discordpy.readthedocs.io/en/latest/) Libary

requests - Requests to the API [click](https://docs.slothpixel.me/)

### Installing packages: 

First, if you didn't already do it, clone the repo to your PC with the following command:

`git clone https://github.com/Lulonaut/Hypixel-Verify.git`

then navigate into the Folder with this Command:

`cd Hypixel-Verify`

and then run the following command to install the packages:


`pip install -r requirements.txt`

Note: You may need to use pip3.6 on Linux

### Bot token

Learn how to get a token [here](https://discordpy.readthedocs.io/en/latest/discord.html#discord-intro)

After that open the "EDITME.py" File and replace the "Please fill me up :(" with it. Please dont remove the quotation marks! An example Line would look like this:

`TOKEN = "0123456789ABCDEF"`

If you followed the Web Page step by step the Bot should already be in your server, so you can start the Bot.py script to start the Bot!

`python Bot.py`


If you still have Problems getting the Bot running or have a general question, contact me on Discord: Lulonaut#3350
