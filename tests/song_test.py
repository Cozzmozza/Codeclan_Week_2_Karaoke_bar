import unittest

from src.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song('song_1', 'artist_1')

    def test_song_has_title(self): #Pass
        self.assertEqual('song_1', self.song.title)
    
    def test_song_has_artist(self): #Pass
        self.assertEqual('artist_1', self.song.artist)

    # def test_song_assigns_key_value_pair(self):
    #     self.assertEqual({'song_1':'artist_1'},self.song.song_info)



# Tests We Want
    # Song has title
    # Song has artist
    # Song_info returns a key value pair, that can be used to add to the song lists later on?