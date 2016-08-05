import logging
import re
import discord


logger = logging.getLogger(__name__)


class ListenerBot:
    def __init__(self):
        self.actions = {}
        self.username = None

    def register_action(self, regex, coro):
        logger.info('Registering action {0}'.format(regex))
        if regex in self.actions:
            logger.info('Overwriting regex {0}'.format(regex))
        self.actions[regex] = (re.compile(regex, re.IGNORECASE), coro)

    async def on_message(self, channel, author, content):
        if author != self.username:
            logger.info('Message received [{0}]: "{1}"'.format(channel, content))
            for regex, fn in self.actions.values():
                match = re.match(regex, content)
                if match:
                    try:
                        await fn(self, channel, author, content, *match.groups())
                    except Exception as e:
                        logger.exception(e)
                        await self.say(channel, 'Something went wrong with that command.')
                    break

    def say(self, channel, message):
        pass


class DiscordBot(ListenerBot):
    def __init__(self):
        self.client = discord.Client()
        self.actions = {}

        @self.client.event
        async def on_ready():
            logger.info('Logged in as')
            logger.info(self.client.user.name)
            logger.info(self.client.user.id)
            logger.info('------')

            self.username = self.client.user.name

        @self.client.event
        async def on_message(message):
            # FIXME: These are still objects, and perhaps they need to be?
            await self.on_message(message.channel, message.author, message.content)

    def run(self, token):
        self.token = token
        self.client.run(self.token)

    def register_action(self, regex, coro):
        logger.info('Registering action {0}'.format(regex))
        if regex in self.actions:
            logger.info('Overwriting regex {0}'.format(regex))
        self.actions[regex] = (re.compile(regex, re.IGNORECASE), coro)

    async def say(self, channel, message):
        await self.client.send_message(channel, message)

    async def say_lines(self, channel, messages):
        for line in messages:
            await self.say(channel, line)
