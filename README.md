# Hypixel-Verify
Verifys Players from the Hypixel Network in Minecraft and gives them a role on your discord!

# Commands


v!verify (Username) // Gives Them the Role you set in Bot.py and a rank role if it exists on the Server!

# Getting the Bot running

### Info
You can use my Bot by inviting it [here](https://discord.com/oauth2/authorize?client_id=734124502027599925&permissions=268438528&scope=bot)
However if you do not trust me or simply want to host it on your own, follow the instructions below. Please note that your PC has to be online 24/7 if you want to host it on your own. So i would consider hosting it on a dedicated Server or somewhere else.


### Python Version

The Python version 3.6 or newer is required, because the Bot uses so called "f-Strings" which were introduced in this Version. After installing Python 3.6 you may need to reinstall the packages.

### Packages
The packages beeing used are:
discord - [discord.py](https://discordpy.readthedocs.io/en/latest/) Libary

requests - Requests to the API ([click][click])

#### Command to install all packages: 

Windows: pip install discord requests

Linux: pip3 install discord requests
Note: You may need to use pip3.6 on Linux

### Bot token

Learn how to get a token [here](https://discordpy.readthedocs.io/en/latest/discord.html#discord-intro)

Aftert that search for KEY = in Bot.py and replace it with your key. The line should look like this: KEY = "your key here".

If you followed the token Page step by step the Bot should already be in your server, so you can start the script to test it and then start hosting it somewhere!

If you still have Problems getting the Bot running or have a general question, contact me on Discord: Lulonaut#3350

[click]: https://docs.slothpixel.me/
