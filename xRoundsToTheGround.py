'''
Adventure
'''
import random
import time

charsList = ['King', 'Knight', 'Princess', 'Thief', 'Prince', 'Queen', 'Wizard', 'CG Artist']
enemiesList = ['Dragon', 'Frog', 'Mushroom', 'Bee', 'Meme', 'Shape-Shifter']
describeList = ['Angry', 'Poisonous', 'Murderous', 'Shy', 'Hesitant', 'Ungrateful', 'Agitated', 'Majestic',
                'Undead', 'Grumpy', 'Vengeful', 'Over-weight', 'Illiterate', 'Blind', 'Unwilling',
                'Old', 'Young', 'Considerate', 'Courteous', 'Amused']
attitudesList = ['disdain', 'apprehension', 'confidence', 'a murderous stare', 'a mocking look',
                'a sad look', 'irritation', 'remorse', 'amusement', 'confidence', 'disgust', 
                'a look of surprise', 'a twinkle in the eyes']
actionsNeg = ['pokes', 'snaps', 'gestures', 'points fingers', 'kicks', 'jabs', 'fires projectiles', 'jeers', 
                'hurls insults', 'throws punches', 'takes a swipe', 'stares', 'claws', 'throws self']
actionsPos = ['heals', 'eats an apple', 'wipes sweat', 'drinks a can of coke', 'downs an energy drink', 
                'grabs a sandwich', 'lets out a battle cry']
battleDesc = ['gruelling', 'gruesome', 'harrowing', 'epic', 'logic-defying', 'earth-shattering']

def randListItem(inList):
    '''
        returns a random item from the incoming list
        inList - <list> a list containing items to be randomly selected

        returns - <object> a single item from the list that is randomly selected
    '''
    return inList[random.randint(0, len(inList)-1)]
# end def randListItem

def introBanner():
    '''
        prints intro banner
    '''
    introStr =  '-------------------------\n'
    introStr += 'Five Rounds to the Ground\n'
    introStr += '-------------------------\n'
        
    print('\n'*2+introStr)
    return
# end def introBanner()

def healthReduce(inHealth, reduceMinMaxList):
    '''
    this will take incoming health and reduce the health by a random value within the reduceMinMaxList
    
    inHealth - <float> incoming health
    reduceMinMaxList - <list of floats> [minReduce, maxReduce] 
                        this is the minimum and maximum amount which to reduce health by

    return - <float> the remaining health after reduce
    '''
    random.seed() # seed from current time
    # this is called unpacking.
    # reduceMin will receive the value in reduceMinMaxList[0]
    # reduceMax will receive the value in reduceMinMaxList[1]
    reduceMin, reduceMax = reduceMinMaxList
    # the next two lines will fit the generated random values
    # into the range defined by the reduceMinMaxList values
    reduceAmt = random.random() * (reduceMax - reduceMin)
    outHealth = inHealth - reduceAmt # reduce inHealth by reduceAmt
    return outHealth
# end def healthReduce()

def statsReport(pChar, pHealth, eChar, eHealth):
    '''
    prints out player and enemy character names and healths respectively
    pChar - <str> name of player
    pHealth - <int> player health
    eChar - <str> name of enemy
    eHealth - <int> enemy health

    return - None
    '''
    print('Player: {} (hp: {:0.2f})'.format(pChar, pHealth))
    print('Enemy: {} (hp: {:0.2f})'.format(eChar, eHealth))
    return
# end of def statsReport()

def actionDamageMessage(char1, char2, damage):
    '''
    Prints a damage dealt message.
    Using char1 and char2 in the function we can re-use this function for player towards enemy
    and enemy towards player.

    char1 - <str> first character that is receiving the damage
    char2 - <str> second character that is dealing the damage
    damage - <float/int> the damage dealt

    return None
    '''
    if damage >= 0:
        finalStr = '{} {} at {}, dealing {:0.2f} damage!'.format(char2, randListItem(actionsNeg), char1, abs(damage))
    else:
        finalStr = '{} {} and recovers {:0.2f} points of health!'.format(char1, randListItem(actionsPos), abs(damage))
    print(finalStr)
    return
# end def actionDamageMessage

def battleEndSummary(playerChar, playerHealth, enemyChar, enemyHealth, numberOfRounds):
    '''
    the summary print out at the end of the battle

    playerChar - <str> player's name
    playerHealth - <float> player's health
    enemyChar - <str> enemy's name
    enemyHealth - <float> player's health
    numberOfRounds - <int> number of rounds that has elapsed
    '''
    endMsg = 'The {} battle ended in {} rounds'.format(randListItem(battleDesc), numberOfRounds)
    print('-' * len(endMsg))
    print(endMsg)
    print('-' * len(endMsg))

    if playerHealth<=0 and enemyHealth<=0:
        defeatStr = '{} and {} are both dead!'.format(playerChar, enemyChar)
    else:
        if playerHealth > enemyHealth:
            defeatStr = '{} has defeated {}!'.format(playerChar, enemyChar)
        else:
            defeatStr = '{} has been defeated by {}'.format(playerChar, enemyChar)
    print(defeatStr)
    print('\n')
    return
# end def battleEndSummary

# -- end of functions

# -- start of main game

# -- generate player --
random.seed(time.time())
descStr = randListItem(describeList)
charStr = randListItem(charsList)
playerChar = '{} {}'.format(descStr, charStr)
playerHealth = 100
# print (playerChar)

# -- display intro
introBanner()

# -- generate enemy
random.seed(time.time()+234)
descStr = None
playerDescStr = playerChar.split()[0]
while not descStr or descStr==playerDescStr:
    # makes sure that enemy's descStr is different from player's descStr
    # to avoid Angry Prince vs Angry Mushroom 
    # or Shy Thief vs Shy Frog
    descStr = randListItem(describeList)
enemyStr = randListItem(enemiesList)
enemyChar = '{} {}'.format(descStr, enemyStr)
enemyHealth = 100
# print (enemyChar)

# -- start Stats
statsReport(playerChar, playerHealth, enemyChar, enemyHealth)
print('')

# --
random.seed(time.time()+3.32)
attitude = randListItem(attitudesList)
print ('The {} approaches the {} with {}'.format(playerChar, enemyChar, attitude))

sleepDelay = 5 # configures the delay for each round
# this dictionary
numberDict = {1:'One', 2:'Two', 3:'Three', 4:'Four', 5:'Five'}
# this is the range of health reduction for each round
healthReduceRangeList = [0.1, 50]
healthIncreaseRangeList = [0.1, 10]
roundsCounter = 0
for this_round in range(5):
    roundNumStr = 'Round {}'.format(numberDict[this_round+1])
    print('-' * len(roundNumStr))
    print(roundNumStr)
    print('-' * len(roundNumStr))
    
    playerHealthOld = playerHealth
    enemyHealthOld = enemyHealth
    
    damagePlayer = 0
    # decides if it is a damage or a heal, healChance is a normalised healing percentage
    healChance = 0.2
    
    # calculate player damage
    randHeal = random.random()
    # print('randheal is {}'.format(randHeal))
    if randHeal <= (healChance):
        # char heals himself

        # takes the health difference of a regular damage, divide by 2 and use it as a health increase
        damagePlayer = -(playerHealthOld - healthReduce(playerHealth, healthIncreaseRangeList))
    else:
        # get randomised health reduction by calling healthReduce()
        damagePlayer = playerHealthOld - healthReduce(playerHealth, healthReduceRangeList)    
    playerHealth = playerHealthOld - damagePlayer
    actionDamageMessage(playerChar, enemyChar, damagePlayer)
    
    # calculate enemy damage
    randHeal = random.random()
    # print('randheal is {}'.format(randHeal))
    if randHeal <= (healChance):
        # char heals himself

        # takes the health difference of a regular damage, divide by 2 and use it as a health increase
        damageEnemy = -(enemyHealthOld - healthReduce(enemyHealth, healthIncreaseRangeList))
    else:
        # get randomised health reduction by calling healthReduce()
        damageEnemy = enemyHealthOld - healthReduce(enemyHealth, healthReduceRangeList) 
    enemyHealth = enemyHealthOld - damageEnemy
    actionDamageMessage(enemyChar, playerChar, damageEnemy)
    print('')

    statsReport(playerChar, playerHealth, enemyChar, enemyHealth)
    print('')
    time.sleep(sleepDelay)

    roundsCounter = this_round+1
    doubleKoFlag = False
    if playerHealth<=0:
        print('{} is dead!'.format(playerChar))
        doubleKoFlag = True
    if enemyHealth<=0:
        print('{} is dead!'.format(enemyChar))
        doubleKoFlag = True
    if doubleKoFlag:
        break
# end for this_round...
print('\n')
battleEndSummary(playerChar, playerHealth, enemyChar, enemyHealth, roundsCounter)
