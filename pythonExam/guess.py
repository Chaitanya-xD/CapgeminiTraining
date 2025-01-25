import random

def game():  
  ans = random.randrange(1,100)
  i = 1

  while True:
    n = int( input(f'Guess {i}: ') )
    if( n < ans ):
      print('Too Low')
    elif( n > ans ):
      print('Too High')
    else:
      print(f"Correct Answer.\nTotal Number of guesses: {i}")
      break
    i += 1

def main():
  print('Game !,Guess the number between 1 and 100\n')
  game()

main()