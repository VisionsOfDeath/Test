import random


def strip_help(bot):
    messages = []

    for regex, action in bot.actions.values():
        if action.__doc__:
            messages.append(action.__doc__.strip())
    return messages


async def bot_help(bot, message):
    await bot.say_lines(message.channel, strip_help(bot))


async def add(bot, channel, author, message):
    """
     - !add, !s - add yourself to the pool
    """
    bot.players.add(author)
    await bot.say(channel, 'You are now signed in, {0}.'.format(author))
    await bot.announce_players(channel)

    if len(bot.players) >= bot.TEAM_SIZE * 2:
        players = random.shuffle(list(bot.players))[:bot.TEAM_SIZE * 2]
        for p in players:
            bot.players.discard(p)
        await bot.say('TEAM ONE: {0}'.format(', '.join([p.name for p in players[:bot.TEAM_SIZE]])))
        await bot.say('TEAM TWO: {0}'.format(', '.join([p.name for p in players[bot.TEAM_SIZE:]])))

        await bot.announce_players(channel)


async def remove(bot, channel, author, message):
    """
     - !remove, !so - remove yourself from the pool
    """
    bot.players.discard(author)
    await bot.say(channel, 'You are now signed out, {0}.'.format(author))
    await bot.announce_players(channel)
