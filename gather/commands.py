from gather.organiser import NotEnoughPlayersError, PlayerNotFound


def strip_help(bot):
    messages = []

    for regex, action in bot.actions.values():
        if action.__doc__:
            messages.append(action.__doc__.strip())
    return messages


async def bot_help(bot, channel, author, message):
    await bot.say_lines(channel, strip_help(bot))


async def game_status(bot, channel, author, message):
    """
     - !game, !status - check current game status
    """
    if bot.organiser.queues[channel]:
        await bot.announce_players(channel)
    else:
        await bot.say(channel, 'No players currently signed in. You can start a game by typing "!add".')


async def add(bot, channel, author, message):
    """
     - !add, !s - add yourself to the pool
    """
    bot.organiser.add(channel, author)
    await bot.say(channel, 'You are now signed in, {0}.'.format(author))
    # Add cooldown in so this will not post more than every five seconds or so
    await bot.announce_players(channel)

    try:
        team_one, team_two = bot.organiser.pop_teams(channel)
        team_one = {str(p) for p in team_one}
        team_two = {str(p) for p in team_two}
        await bot.say(
            channel,
            'Game starting!\nTeam 1: {}\nTeam 2: {}'.format(team_one, team_two))
    except NotEnoughPlayersError:
        pass


async def remove(bot, channel, author, message):
    """
     - !remove, !so - remove yourself from the pool
    """
    try:
        bot.organiser.remove(channel, author)
        await bot.say(channel, 'You are now signed out, {0}.'.format(author))
        # Add cooldown in so this will not post more than every five seconds or so
        await bot.announce_players(channel)
    except PlayerNotFound:
        await bot.say(
            channel,
            "Doesn't look like you are signed in. "
            "Try signing in with !add, {}.".format(author))
