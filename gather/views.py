import random
from gather import bot


@bot.action('^!help')
async def bot_help(message):
    for regex, action in bot.actions.values():
        if action.__doc__:
            await bot.say(message.channel, action.__doc__.strip())


@bot.action('^!(?:add|s)')
async def add(message):
    """
     - !add, !s - add yourself to the pool
    """
    bot.players.add(message.author)
    await bot.say(message.channel, 'You are now signed in, {0}.'.format(message.author))
    await bot.announce_players(message.channel)

    if len(bot.players) >= bot.TEAM_SIZE * 2:
        players = random.shuffle(list(bot.players))[:bot.TEAM_SIZE * 2]
        for p in players:
            bot.players.discard(p)
        await bot.say('TEAM ONE: {0}'.format(', '.join([p.name for p in players[:bot.TEAM_SIZE]])))
        await bot.say('TEAM TWO: {0}'.format(', '.join([p.name for p in players[bot.TEAM_SIZE:]])))

        await bot.announce_players(message.channel)


@bot.action('^!(?:remove|so)')
async def remove(message):
    """
     - !remove, !so - remove yourself from the pool
    """
    bot.players.discard(message.author)
    await bot.say(message.channel, 'You are now signed out, {0}.'.format(message.author))
    await bot.announce_players(message.channel)
