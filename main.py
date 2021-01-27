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

    #There is only one type,because there are no reason do is for
    #second. It well work with first
    # if you would add data for second type in content type.. Just delete it
    typeSMS = 0

    #create TRAAAAAAAAAAAPPPPPPPPP WAHAHAHHAHA
    #Actualy our lifes is trap   _)
    for i in range(len(cnt.endText[typeSMS])):
        index = random.randint(0, len(cnt.endText[typeSMS][i]) - 1)
        if len(cnt.endText[typeSMS][i][index]) != 0:
            text += cnt.endText[typeSMS][i][index] + ' '
    #retunt created sms
    return text


for i in range(10):
    print('\t---')
    print(generateSMS())