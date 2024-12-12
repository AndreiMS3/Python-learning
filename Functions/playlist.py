from functools import reduce

# List of songs with their durations (in minutes)
playlist = [
    ('What Was I Made For?', 3.42), 
    ('Just Like That', 5.05), 
    ('Song 3', 6.8), 
    ('Leave The Door Open', 4.02), 
    ('I Can\'t Breath', 4.47), 
    ('Bad Guy', 3.14)
    ]

def longer_than_five_minutes(song):
    return song[1] >= 5.0
            
         
longer_songs =  filter(longer_than_five_minutes,playlist)
longer_songs_list = list(longer_songs)
print(longer_songs_list)

#Use map() to convert all the durations of the songs in your playlist from minutes to seconds.

#Define the method that converts minutes in seconds.
def minutes_to_seconds(song):
    return song[1] * 60

#Define the map() method.
songs_in_seconds = map(minutes_to_seconds, playlist)

#Convert to list and print it.
songs_in_seconds_list = list(songs_in_seconds)
print(songs_in_seconds_list)

#Add up the total playtime of the playlist with reduce().
#add_durations() method to be used in reduce().

def add_duration(total, song):
    return total + song[1]

total_playtime= reduce(add_duration, playlist,0)
print(total_playtime)