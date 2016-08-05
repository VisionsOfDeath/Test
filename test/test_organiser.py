import unittest
from gather.organiser import Queue, Organiser


class TestQueue(unittest.TestCase):
    def test_add(self):
        o = Queue()
        self.assertEqual([], o.players)
        o = o.add('testplayer')
        self.assertEqual(['testplayer'], o.players)

    def test_remove(self):
        o = Queue(['testplayer'])
        self.assertEqual(['testplayer'], o.players)
        o = o.remove('testplayer')
        self.assertEqual([], o.players)

    def test_remove_failure(self):
        o = Queue(['testplayer'])
        self.assertRaises(ValueError, o.remove, 'does not exist')


class StubQueue(set):
    def add(self, value):
        super().add(value)
        return self

    def remove(self, value):
        super().remove(value)
        return self


class TestOrganiser(unittest.TestCase):
    def test_add(self):
        organiser = Organiser(lambda: StubQueue())

        self.assertEqual(set(), organiser.queues['test'])
        organiser.add('test', 'testplayer')
        self.assertEqual(set(['testplayer']), organiser.queues['test'])
