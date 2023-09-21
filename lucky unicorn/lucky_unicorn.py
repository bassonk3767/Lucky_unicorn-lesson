import random as rnd

# rounds
i = 0

# points
point = 0


def play(a,b):
    bb =  'ff'
    if a >= 5 and b == 4:
        print('\n\nYOU WIN!!\n')
    else:

        # Asking user if they know how to play.

        print('\n\nDo you know how to play\n\n[1]> Yes , [2]> No')

        knowledge = input()

        if knowledge == '1':
            print('\n\nPlease insert the amount that you wish to bet:\n\n')
            bet = int(input())

        # Generating dealer's value

            dealers = rnd.randint( bet - 2 , bet + 2)

            # Players cards

            c1 = rnd.randint(bet- 3 , bet * 2)
            c2 = rnd.randint(bet - 3 , bet * 3)

            # Dealer's cards

            d1 = bet * 2
            d2 = bet + 4

            print("\n\nHere are your cards:\n\nCard 1: %d,\n\nCard 2: %d", %c1 , %c2)

        # if user enters 1 or 2
        elif knowledge == '2':
             print('\n\nHere is how to play the game:\n\n1. Place a bet between $1 all the way up to $10,\n2. Dealer places a bet aswell,\n3. You will have 2 cards including the dealer,\n4. Each card will have a set of digits,\ni5. If your cards combined are greater in value than the cards of the dealer then you win')
             print('\n\nContinue?\n\n[1]> Yes , [2]> No\n')
             conf = input()
             if conf == '1':
                play(a,b)

             elif conf == '2':
                  return 0

while i < 10:
    print('\n\nPlease deposit $1 to play LUCKY UNICORN!!\n\n[1]> Yes , [2]> No\n\n')
    ii = input()
    if ii == '1':
        i += 1
        play(i,point)
    elif ii == '2':
          print('\n\nDeactivating game\n\n')
          break
    else:
        print(''
              '\n\nPlease insert your choice that was mentioned on screen')





