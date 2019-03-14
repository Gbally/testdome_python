"""
Python skill test from:
https://www.testdome.com/questions/python/song/25557?visibility=1&skillId=9

Author:
Anonymous

Score:
XXX% (X pass / X fail)

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
        return None
            
first = Song("Hello")
second = Song("Eye of the tiger")
    
first.next_song(second);
second.next_song(first);
    
print(first.is_repeating_playlist())