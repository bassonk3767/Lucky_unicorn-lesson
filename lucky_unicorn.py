# rounds
i = 0

# points
point = 0


def play(a,b):
    bb =  'ff'
    if a >= 5 and point == 4:
        print('\n\nYOU WIN!!\n')
    else:
        print('\n\nPlease insert the amount that you wish to bet:\n\n')
        bet = int(input())
        

while i < 10:
    print('\n\nPlease deposit $1 to play LUCKY UNICORN!!\n\n[1]> Yes , [2]> No\n\n')
    ii = int(input())
    if ii == 1:
        i += 1
        play()
    elif ii == 2:
          print('\n\nDeactivating game\n\n')
          break
    else:
        print(''
              '\n\nPlease insert your choice that was mentioned on screen')