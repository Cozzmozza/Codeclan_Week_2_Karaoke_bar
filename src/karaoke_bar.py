class KaraokeBar:
    def __init__(self, karaoke_bar_name, room, till_cash):
        self.karaoke_bar_name = karaoke_bar_name
        self.room = room
        self.till_cash = till_cash

    def add_to_song_list(self, song):
        self.room.song_list[song.title] = song.artist

    def remove_from_song_list(self, song):
        self.room.song_list.pop(song.title)
  
    def add_guest(self, guest):
        if len(self.room.guest_list) < self.room.room_capacity:
            self.room.guest_list.append(guest)
        else:
            return 'Sorry, this room is now at full capacity'

    def remove_guest(self, guest):
        self.room.guest_list.remove(guest)

    def remove_cash_from_guest(self, guest):
        cost = self.room.room_cost
        if guest.wallet_balance >= cost:
            guest.remove_cash_from_wallet(cost)
        else:
            return f'{guest.name} does not have enough money for this'

    def add_cash_to_till_by_one_sale(self):
        self.till_cash += self.room.room_cost

    def remove_from_till(self, amount):
        self.till_cash -= amount

    def sell_to_group_of_guests(self, guests):
        if len(guests) <= self.room.room_capacity:
            for guest in guests:
                self.remove_cash_from_guest(guest)
                self.add_cash_to_till_by_one_sale()
                self.add_guest(guest)
        elif len(guests) > self.room.room_capacity:
            return 'Sorry there are too many of you!'

    def guest_fave_song_check(self, guest):
        if guest.fave_song_name in self.room.song_list:
                    return f'YAY my FAVOURITE! - says {guest.name}' 
    
    def multiple_guest_fave_song_check(self, guests):
        favourite_total = 0
        for guest in guests:    
            if guest.fave_song_name in self.room.song_list:
                favourite_total += 1
        if favourite_total > 2:
            return 'THERE ARE MANY FAVOURITES!'
        elif favourite_total == 2:
            return 'YAY there are two favourites!'
        elif favourite_total == 1:
            return 'Yay one favourite'
  
