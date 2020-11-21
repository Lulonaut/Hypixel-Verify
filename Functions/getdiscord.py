import requests
from requests.exceptions import ReadTimeout

data = None
defaultTimeout = 20


def fetch(url, timeout=None):
    if timeout:
        return (lambda u: requests.get(url, timeout=timeout).json())(url)
    return (lambda u: requests.get(url).json())(url)


def discordlinked(name):
    """Check linked Discord of Player

    Args:

        name (String): In-Game name of player

    Raises:

        APITimeoutError: Raised after 20 seconds without a response
        APIError: Raised if some other Error occours while calling API
        DiscordError: Raised if Discord tag doesn't exist (eg: wrong Username)

    Returns:

        String: Discord Tag of Player
        None: If no Discord Tag was found
    """
    timeouted = None
    try:
        data = fetch(
            f"https://api.slothpixel.me/api/players/{name}", timeout=defaultTimeout)

    except ReadTimeout:
        timeouted = True

    except:
        timeouted = False

    if timeouted:
        raise APITimeoutError(
            f"No response after {defaultTimeout} seconds (Requested Player: {name})")
    elif timeouted == False:
        raise APIError("Unknown Error while calling API")
    try:
        error = data['error']
        if error:
            raise APIError(f"API reported: {error}")
    except:
        pass

    try:
        return data["links"]["DISCORD"]
    except:
        raise DiscordError("No Discord field in JSON response")


def rank(name):
    """
    Find out the rank of a player

    Args:

        name (String): In-Game name of player

    Raises:

        APITimeoutError: Raised after 20 seconds without a response
        APIError: Raised if some other Error occours while calling API
        RankError: Raised if the rank does not exist (eg: wrong username)

    Returns:

        String: Rank of Player
        None: If no rank was found
    """
    timeouted = None
    try:
        data = fetch(
            f"https://api.slothpixel.me/api/players/{name}", timeout=defaultTimeout)

    except ReadTimeout:
        timeouted = True
    except:
        timeouted = False

    if timeouted:
        raise APITimeoutError(
            f"No response after {defaultTimeout} seconds (Requested Player: {name})")
    elif timeouted == False:
        raise APIError("Unknown Error while calling API")
    try:
        error = data['error']
        if error:
            raise APIError(f"API reported: {error}")
    except:
        pass

    try:
        rank = data["rank"]
        if rank == "VIP_PLUS":
            return "VIP+"
        elif rank == "MVP_PLUS":
            return "MVP+"
        elif rank == "MVP_PLUS_PLUS":
            return "MVP++"
        return rank

    except:
        raise RankError(f"Can't get valid rank for {name}")


def name(name):
    """
    Correct capitalisation for username

    Args:

        name (String): In-Game name of player

    Raises:

        APITimeoutError: Raised after 20 seconds without a response
        APIError: Raised if some other Error occours while calling API
        NameError: Raised if the name can't be found (eg: wrong username)

    Returns:

        String: Username with correct capitalisation
    """
    timeouted = None
    try:
        data = fetch(
            f"https://api.slothpixel.me/api/players/{name}", timeout=defaultTimeout)

    except ReadTimeout:
        timeouted = True
    except:
        timeouted = False

    if timeouted:
        raise APITimeoutError(
            f"No response after {defaultTimeout} seconds (Requested Player: {name})")
    elif timeouted == False:
        raise APIError("Unknown Error while calling API")

    try:
        error = data['error']
        if error:
            raise APIError(f"API reported: {error}")
    except:
        pass

    try:
        name = data["username"]
        return name
    except:
        print(f"Error getting correct name for {name}")
        raise NameError((f"Can't get valid name for  {name}"))


def guild(name):
    """
    Check the current Guild of a player

    Args:

        name (String): In-Game name of player

    Raises:

        APITimeoutError: Raised after 20 seconds withouta response
        APIError: Raised if some other Error occours while calling API
        GuildError: Raised if the guild can't be found (eg: wrong username)

    Returns:

        String: Guild Name
    """

    timeouted = None
    try:
        data = fetch(
            f"https://api.slothpixel.me/api/guilds/{name}", timeout=defaultTimeout)

    except ReadTimeout:
        timeouted = True
    except:
        timeouted = False

    if timeouted:
        raise APITimeoutError(
            f"No response after {defaultTimeout} seconds (Requested Player: {name})")
    elif timeouted == False:
        raise APIError("Unknown Error while calling API")

    try:
        error = data['error']
        if error:
            raise APIError(f"API reported: {error}")
    except:
        pass
    guildName = None

    try:
        guildName = data["name"]
    except:
        try:
            guildName = data['guild']
            if guildName == "null":
                print("null")
                guildName = None
        except:
            raise GuildError(f"Can't get valid guild for {name}")

    return guildName


# Custom Errors
class APIError(Exception):
    pass


class RankError(Exception):
    pass


class APITimeoutError(Exception):
    pass


class NameNotFoundError(Exception):
    pass


class DiscordError(Exception):
    pass


class GuildError(Exception):
    pass
