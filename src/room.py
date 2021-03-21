class Room:
    def __init__(self, room_number, song_list):
        self.room_number = room_number
        self.song_list = song_list #We have an initial song list assigned to the room
        
        self.guest_list = [] #There are no guests initially
        self.room_capacity = 4 # The room capcity of all rooms is 4
        self.room_cost = 10 #Flat rate for all rooms, per room

        
