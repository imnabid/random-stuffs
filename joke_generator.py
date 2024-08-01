import requests
import time

def jokes(no_of_jokes): #python generator   
    print('I ran just once, mate\n') 
    for _ in range(no_of_jokes):
        try:
             res = requests.get('https://v2.jokeapi.dev/joke/Any')
             res = res.json()
             dashed = '\n----------------------------------------------'
             joke = res['setup'] + '\n' + res['delivery'] + dashed
             yield joke
        except KeyError:
             yield 'Joke not found\n'

for joke in jokes(5):
     print(joke)
     time.sleep(2)