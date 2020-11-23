import pyttsx3

engine = pyttsx3.init()

rate = engine.getProperty('rate')

print('The current rate is: ', rate, ' Which is the default rate')
rateInput = input('Change Rate? Y/N: ')

if rateInput == 'Y' or rateInput == 'y':  # change the rate of speech
    newRate = input('Enter New Rate:  ')
    engine.setProperty('rate', newRate)
elif rateInput == 'N' or rateInput == 'n':
    engine.setProperty('rate', 200)

tts = input('Text To Speak: ')

while tts == '' or tts == ' ':  # if text to speak is blank or whitespace it keep asking for text
    tts = input('Text To Speak: ')

engine.say(tts)
engine.runAndWait()
