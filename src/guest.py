class Guest:
    def __init__(self, name, wallet_balance, fave_song_name, fave_song_artist):
        self.name = name
        self.wallet_balance = wallet_balance
        self.fave_song_name = fave_song_name
        self.fave_song_artist = fave_song_artist
    
    def remove_cash_from_wallet(self, amount):
        self.wallet_balance -= amount