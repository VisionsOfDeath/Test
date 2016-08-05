import unittest
from gather.organiser import Organiser


class TestOrganiser(unittest.TestCase):
    def test_add(self):
        o = Organiser()
        self.assertEqual([], o.players)
        o = o.add('testplayer')
        self.assertEqual(['testplayer'], o.players)

    def test_remove(self):
        o = Organiser(['testplayer'])
        self.assertEqual(['testplayer'], o.players)
        o = o.remove('testplayer')
        self.assertEqual([], o.players)

    def test_remove_failure(self):
        o = Organiser(['testplayer'])
        self.assertRaises(ValueError, o.remove, 'does not exist')
