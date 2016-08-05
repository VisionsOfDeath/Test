import asyncio
import unittest
from unittest import mock
from gather import commands


def async_test(f):
    # http://stackoverflow.com/a/23036785/304210
    def wrapper(*args, **kwargs):
        coro = asyncio.coroutine(f)
        future = coro(*args, **kwargs)
        loop = asyncio.get_event_loop()
        loop.run_until_complete(future)
    return wrapper


class TestGatherBot(unittest.TestCase):
    def test_help(self):
        commands.strip_help(mock.Mock(actions={
            'friendly': ['testregex', mock.Mock(__doc__='Hello!')]
        }))


if __name__ == '__main__':
    unittest.main()
