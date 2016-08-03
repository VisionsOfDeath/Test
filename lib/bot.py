import logging
import re
import discord


logger = logging.getLogger(__name__)


class Bot:
    def __init__(self):
        self.client = discord.Client()
        self.actions = {}

        @self.client.event
        async def on_ready():
            logger.info('Logged in as')
            logger.info(self.client.user.name)
            logger.info(self.client.user.id)
            logger.info('------')

        @self.client.event
        async def on_message(message):
            if message.author != self.client.user:
                logger.info('Message received [{0}]: "{1}"'.format(message.channel, message.content))
                for regex, fn in self.actions.values():
                    match = re.match(regex, message.content)
                    if match:
                        try:
                            await fn(message, *match.groups())
                        except Exception as e:
                            logger.exception(e)
                            await self.say(message.channel, 'Something went wrong with that command.')
                        break

    def run(self, username, password):
        self.username = username
        self.password = password
        self.client.run(self.username, self.password)

    def action(self, regex, coro):
        logger.info('Registering action {0}'.format(regex))
        if regex in self.actions:
            logger.info('Overwriting regex {0}'.format(regex))
        self.actions[regex] = (re.compile(regex, re.IGNORECASE), coro)

    async def say(self, channel, message):
        await self.client.send_message(channel, message)

    async def say_lines(self, channel, messages):
        for line in messages:
            await self.say(channel, line)
