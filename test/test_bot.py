import asyncio
import re
import unittest
from unittest import mock
from gather.bot import ListenerBot


def async_test(f):
    # http://stackoverflow.com/a/23036785/304210
    def wrapper(*args, **kwargs):
        coro = asyncio.coroutine(f)
        future = coro(*args, **kwargs)
        loop = asyncio.get_event_loop()
        loop.run_until_complete(future)
    return wrapper


class TestGatherBot(unittest.TestCase):
    def test_register(self):
        bot = ListenerBot()
        self.assertEqual({}, bot.actions)
        regex = r'^test'
        action = mock.Mock()
        bot.register_action(regex, action)
        self.assertEqual(
            {regex: (re.compile(regex, re.IGNORECASE), action)},
            bot.actions
        )

    @async_test
    def test_on_message_from_bot(self):
        bot = ListenerBot()
        bot.username = 'testuser'
        regex = r'^test'
        action = mock.Mock()
        bot.actions = {regex: (re.compile(regex, re.IGNORECASE), action)}
        bot.on_message(mock.Mock(), mock.Mock, 'test')
        action.assert_not_called()


if __name__ == '__main__':
    unittest.main()
