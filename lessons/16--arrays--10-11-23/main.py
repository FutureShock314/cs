from random import randint

# task 1

songs =                                                                                                                                                                                                                                                                              ['Radioactive', 'Believer', 'Nanolove', 'Bossfight', 'Space Invaders', 'Natural']

song = songs[randint(0, len(songs) - 1)]
guess = input(f'guess song of {songs} \n>> ')


while guess.capitalize() != song:

    if guess.lower() == 'no':
        print('ok')
    elif guess.capitalize() == song:
        print('you win ig')
    else:
        print('bad')
        guess = input(f'guess song of {songs} \n>> ')
