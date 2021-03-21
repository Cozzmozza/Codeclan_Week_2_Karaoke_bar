import unittest

from src.guest import Guest

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest('Cozza', 18.50, 'Black & White', 'In Flames')

    def test_guest_has_name(self): 
        self.assertEqual('Cozza', self.guest.name)

    def test_guest_has_wallet_balance(self): 
        self.assertEqual(18.50, self.guest.wallet_balance)

    def test_guest_can_remove_cash_from_wallet(self): 
        self.guest.remove_cash_from_wallet(10.00)
        self.assertEqual(8.50, self.guest.wallet_balance)

    def test_guest_has_favourite_song_name(self):
        self.assertEqual('Black & White', self.guest.fave_song_name)

    def test_guest_has_favourite_song_artist(self):
        self.assertEqual('In Flames', self.guest.fave_song_artist)