import random
n = 20

to_be_guessed = int(n * random.random()) + 1

guess = 0

while guess != to_be_guessed:
    guess = int(input('new number:'))
    if guess > 0:
        if guess > to_be_guessed:
            print('the number is too large')
        elif guess < to_be_guessed:
            print('number is too small')
    else:
      print('sorry thats youre giving up')
else:
  print('congrulation, you made it!!!!!!!!!!!!!!')