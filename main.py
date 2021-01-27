import content as cnt
import random

def generateSMS():
    text = ''

    #create begin of SMS
    for i in range(len(cnt.startText)):
        index = random.randint(0, len(cnt.startText[i]) - 1)
        if len(cnt.startText[i][index]) != 0:
            text += cnt.startText[i][index] + ' '
    #chose type of SMS
    #create middle of SMS`s text
    typeSMS = random.randint(0, len(cnt.middleText) - 1)
    for i in range(len(cnt.middleText[typeSMS])):
        index = random.randint(0, len(cnt.middleText[typeSMS][i]) - 1)
        if len(cnt.middleText[typeSMS][i][index]) != 0:
            text += cnt.middleText[typeSMS][i][index] + ' '
    #create TRAAAAAAAAAAAPPPPPPPPP AHAHAHHAHA
    #Actualy our lifes is trap   _)
    for i in range(len(cnt.endText[typeSMS])):
        index = random.randint(0, len(cnt.endText[typeSMS][i]) - 1)
        if len(cnt.endText[typeSMS][i][index]) != 0:
            text += cnt.endText[typeSMS][i][index] + ' '
    print(text)

for i in range(10):
    print('\t---')
    generateSMS()