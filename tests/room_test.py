import unittest

from src.room import Room
from src.guest import Guest #Used to add guests to the list of guests
from src.song import Song #Used to add a song to the songlist

class TestRoom(unittest.TestCase):

    def setUp(self):
        songs = { # The initial song dictionary we'll have as a template for all rooms if we want to
            'song_1' : 'artist_1',
            'song_2' : 'artist_2',
            'song_3' : 'artist_3'
            }
        self.room = Room(1, songs)

    def test_room_has_number(self): #Pass
        self.assertEqual(1, self.room.room_number)

    def test_room_has_initial_song_list(self): #Pass
        self.assertEqual(3, len(self.room.song_list))
