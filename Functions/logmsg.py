import datetime

FILE = "latest.log"

def logmsg(message):
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    msg=(f"[{time}] {message}\n")
    f = open(FILE,"a")
    f.write(msg)
    print(msg)
    f.close


def clear():
    f = open(FILE,"w")
    f.write("//Beginning of Log\n")
    f.close()
