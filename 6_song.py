"""
Python skill test from:
https://www.testdome.com/questions/python/song/25557?visibility=1&skillId=9

Author:
Anonymous

Score:
100% (4 pass / 0 fail)

Question:
A playlist is considered a repeating playlist if any of the songs contain a reference 
to a previous song in the playlist. Otherwise, the playlist will end with the last song 
which points to None.

Implement a function is_repeating_playlist that, efficiently with respect to time used, 
returns true if a playlist is repeating or false if it is not.

For example, the following code prints "True" as both songs point to each other.

> first = Song("Hello")
> second = Song("Eye of the tiger")
    
> first.next_song(second);
> second.next_song(first);
    
> print(first.is_repeating_playlist())
"""

######## Start Original script ########

# class Song:
#     def __init__(self, name):
#         self.name = name
#         self.next = None

#     def next_song(self, song):
#         self.next = song 
    
#     def is_repeating_playlist(self):
#         """
#         :returns: (bool) True if the playlist is repeating, False if not.
#         """
#         return None
            
# first = Song("Hello")
# second = Song("Eye of the tiger")
    
# first.next_song(second);
# second.next_song(first);
    
# print(first.is_repeating_playlist())

######## End Original script ########

class Song:
    def __init__(self, name):
        self.name = name
        self.next = None

    def next_song(self, song):
        self.next = song 
    
    def is_repeating_playlist(self):
        """
        :returns: (bool) True if the playlist is repeating, False if not.
        """
        # With large dataset, use of set() is required instead of a list()
        song_set = set()
        current_song = self

        while current_song:
            if current_song.name in song_set:
                return True # If the current song is in song_set (already played, return True)
            
            # Add current song to the list and change song
            song_set.add(current_song.name) # append with list(), add with set()
            current_song = current_song.next

        # Return False if no double song have been found
        return False

            
first = Song("Hello")
second = Song("Eye of the tiger")
    
first.next_song(second);
second.next_song(first);
    
print(first.is_repeating_playlist())