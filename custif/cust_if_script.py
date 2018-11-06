#!/usr/bin/env python3
movie_select = ('Harry Poter', 'Hobbit', 'Narnia', 'Indiana Jones'
message('What move do you want to watch')
movie = float(input())
if movie = [0]
    movie = movie_select[0]
elif movie = [1]
    movie = movie_select[1]
elif movie = [2]
    movie = movie_select[2]
else:
    movie = [3]
    movie = movie_select[3]
print(movie)

message = 'The movie is about to begin, we recommend '
print('What is your connection speed in Mbps?')
connection = float(input())
if connection >= 25:
    message = message + 'setting video to 4k.'
elif connection >= 5:
    message = message + 'setting video to 1080p.'
elif connection >= 2:
    message = message + 'setting video to 720p.'
else:
    message = message + 'finding another access network.'
print(message)

