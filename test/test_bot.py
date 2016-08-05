import re
import unittest
from gather.bot import ListenerBot


class TestGatherBot(unittest.TestCase):
    def test_register(self):
        bot = ListenerBot()
        self.assertEqual({}, bot.actions)
        regex = r'^test'
        action = unittest.mock.Mock()
        bot.register_action(regex, action)
        self.assertEqual(
            {regex: (re.compile(regex, re.IGNORECASE), action)},
            bot.actions
        )


if __name__ == '__main__':
    unittest.main()
