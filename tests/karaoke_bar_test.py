import unittest

from src.karaoke_bar import KaraokeBar
from src.song import Song
from src.guest import Guest
from src.room import Room

class TestKaraokeBar(unittest.TestCase):
    def setUp(self):
        songs = {
            'Dark Side of the Moon' : 'Pink Floyd',
            'Beer' : 'Psychostick',
            'Black & White' : 'In Flames',
            'Hey Ya' : 'Outkast',
            'Firework' : 'Katy Perry',
            'Delete me' : 'ASAP'
            }
        room = Room(1, songs) #We are working with room 1, which has the songs above as default
        till_cash = 500
        self.karaoke_bar = KaraokeBar('Screeching Soul Tavern', room, till_cash)
        self.guest_1 = Guest('Cozza', 18.50, 'Black & White', 'In Flames')
        self.guest_2 = Guest('Mozza', 12.00, 'Some other song', 'Unknown Artist')
        self.guest_3 = Guest('Tozza', 25.00, 'Walk', 'Pantera')
        self.guest_4 = Guest('Lozza', 16.73, 'Dark Side of the Moon', 'Pink Floyd')
        self.guest_5 = Guest('Pozza', 109.20, 'Blah blah', 'Bleh')
        self.guest_6 = Guest('Jozza', 3.00, 'Irrelevant', 'Not important')
        self.guest_list_4 = [self.guest_1, self.guest_2, self.guest_3, self.guest_4]
        # self.guest_list_5 = self.guest_list_4.append(self.guest_5) #This did not work 
        self.guest_list_5 = [self.guest_1, self.guest_2, self.guest_3, self.guest_4, self.guest_5]

    def test_karaoke_bar_has_name(self): 
        self.assertEqual('Screeching Soul Tavern', self.karaoke_bar.karaoke_bar_name)

    def test_can_add_songs_to_room_song_list_using_Song(self): 
        new_song_1 = Song('Paranoid', 'Ozzy Ozzy Ozzy')
        new_song_2 = Song('Walk', 'Pantera')
        self.karaoke_bar.add_to_song_list(new_song_1)
        self.karaoke_bar.add_to_song_list(new_song_2)
        self.assertEqual(8, len(self.karaoke_bar.room.song_list))

    def test_can_remove_song_from_song_list_using_Song(self): 
        unwanted_song_1 = Song('Firework', 'Katy Perry')
        unwanted_song_2 = Song('Delete me', 'ASAP')
        self.karaoke_bar.remove_from_song_list(unwanted_song_1)
        self.karaoke_bar.remove_from_song_list(unwanted_song_2)
        self.assertEqual(4, len(self.karaoke_bar.room.song_list))

    def test_room_has_no_initial_guests(self): 
        self.assertEqual([], self.karaoke_bar.room.guest_list)

    def test_can_add__one_guest(self): 
        self.karaoke_bar.add_guest(self.guest_1)
        self.assertEqual(1, len(self.karaoke_bar.room.guest_list))

    def test_can_add__4_guests(self): 
        for guest in self.guest_list_4:
            self.karaoke_bar.add_guest(guest)
        self.assertEqual(4, len(self.karaoke_bar.room.guest_list))
    
    def test_will_not_add_guests_if_full__5(self): 
        for guest in self.guest_list_5:
            self.karaoke_bar.add_guest(guest)
        self.assertEqual('Sorry, this room is now at full capacity', self.karaoke_bar.add_guest(guest))
        self.assertEqual(4, len(self.karaoke_bar.room.guest_list))
                # See below comments. This test may be redundant if below logic is true
    
    def test_will_not_add_guests_if_full__4(self):
        for guest in self.guest_list_4:
            self.karaoke_bar.add_guest(guest)
        self.assertEqual('Sorry, this room is now at full capacity', self.karaoke_bar.add_guest(guest)) 
                #Does this actually tests for a 5th guest?
                #Our loop calls our add_guest function 4 times, then again a 5th for the assertEqual? Test passes anyway
                #Confirmation test below to check the room list is indeed 4, and it hasn't rejected the 4th guest
        self.assertEqual(4, len(self.karaoke_bar.room.guest_list))

    def test_can_remove_guest(self):
        self.karaoke_bar.add_guest(self.guest_1)
        self.karaoke_bar.remove_guest(self.guest_1)
        self.assertEqual(0, len(self.karaoke_bar.room.guest_list))
   
    def test_can_reduce_customer_wallet_reduce(self):
        self.karaoke_bar.remove_cash_from_guest(self.guest_1)
        self.assertEqual(8.50, self.guest_1.wallet_balance)
    
    def test_customer_wallet_must_have_sufficient_funds(self):
        self.assertEqual('Jozza does not have enough money for this', self.karaoke_bar.remove_cash_from_guest(self.guest_6))
    
    def test_can_add_cash_to_till_for_a_sale(self): 
        self.karaoke_bar.add_cash_to_till_by_one_sale()
        self.assertEqual(510, self.karaoke_bar.till_cash)
        
    def test_can_remove_cash_from_till(self):
        amount = 150
        self.karaoke_bar.remove_from_till(amount)
        self.assertEqual(350, self.karaoke_bar.till_cash)
    
    def test_can_make_a_karaoke_room_sale_to_4_guests(self):
        # Test to see if the bar can take in 4 guests with varied wallets, and make 4 sales
        guests = self.guest_list_4
        self.karaoke_bar.sell_to_group_of_guests(guests)
        self.assertEqual(8.50, guests[0].wallet_balance)       
        self.assertEqual(2.00, guests[1].wallet_balance)      
        self.assertEqual(15.00, guests[2].wallet_balance)     
        self.assertEqual(6.73, guests[3].wallet_balance)       
        self.assertEqual(540, self.karaoke_bar.till_cash)           
        self.assertEqual(4, len(self.karaoke_bar.room.guest_list))     

    def test_more_guests_than_room_limit_means_no_entry_to_all(self):
        guests = self.guest_list_5
        group_5_run = self.karaoke_bar.sell_to_group_of_guests(guests)
        self.assertEqual(0, len(self.karaoke_bar.room.guest_list))
        self.assertEqual('Sorry there are too many of you!', group_5_run)


    def test_guest_fave_song_found(self):
        output = self.karaoke_bar.guest_fave_song_check(self.guest_1)
        self.assertEqual('YAY my FAVOURITE! - says Cozza', output)

    def test_matching_guests_favourite_songs(self):
        guests = self.guest_list_4
        output = self.karaoke_bar.multiple_guest_fave_song_check(guests)
        self.assertEqual('YAY there are two favourites!', output)

    def test_new_favourite_from_added_song(self): 
        guests = self.guest_list_4
        new_song_2 = Song('Walk', 'Pantera')
        self.karaoke_bar.add_to_song_list(new_song_2)
        output = self.karaoke_bar.multiple_guest_fave_song_check(guests)
        self.assertEqual('THERE ARE MANY FAVOURITES!', output)


    def test_1_less_favourite_from_removed_song(self): 
        guests = self.guest_list_4
        song_to_delete = Song('Black & White', 'In Flames')
        self.karaoke_bar.remove_from_song_list(song_to_delete)
        output = self.karaoke_bar.multiple_guest_fave_song_check(guests)
        self.assertEqual('Yay one favourite', output)