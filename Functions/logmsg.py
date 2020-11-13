import datetime
try:
    import loadconf
except:
    from Functions import loadconf


def logmsg(message, counting=False):
    # format message
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    msg = (f"[{time}] {message}\n")
    printed = False

    # load config
    conf = loadconf.load()

    # return if logging is not enabled
    if conf['logging']['masterToggle'] == False:
        return
    # print if its a counting message and its enabled, return if it shouldnt be printed to File
    if conf['logging']['console']['logMessagesToConsole'] == True and counting == True:
        print(msg)
        printed = True


    # print Message if it's enabled and its not a counting message (checked above)
    if (
        conf['logging']['console']['logToConsole'] == True
        and counting == False
        and not printed
    ):
        print(msg)

    if (
        conf['logging']['console']['logMessagesToConsole'] == True
        and counting == True
        and not printed
    ):
        print(msg)



    # Log message to File if it's enabled
    if conf['logging']['file']['logToFile'] == True:
        if conf['logging']['file']['logMessagesToFile'] == False and counting == True:
            return
        FILE = conf['logging']['file']['fileForLogging']
        f = open(FILE, "a")
        f.write(msg)
        f.close

