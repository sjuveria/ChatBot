import random

r_eat = 'I dont eat because i am a robot'
r_weather = 'it\'s sunny today'

def r_joke():
    joke = ['They say that age is nothing but a number. But technically its also a word.',
              'The world changes. Sometimes it changes a lot. But last time I checked it was still around',
              'What do kids play when their mom is using the phone? Bored games.'][random.randrange(3)]
    return joke

def unknown():
    response = ['could you please say it again?','what does it mean?',
                'sorry,i didn\'t get that'][random.randrange(3)]
    return response