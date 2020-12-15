from gtts import gTTS
import playsound, os
from .methods import define, now, timer_start
from .twitter.main import tweet
num = 1
class Cortana:
    def __init__(self, *lang, **kw):
        if lang:
            self.lang=lang[0]
        else:
            self.lang='pt'
        #mode
        try:
            mode=kw.get('mode')[0]
        except:
            pass
        '''if mode:
            if mode=='text':
                self.greet('text')
                self.wait_for_input()
            else:
                self.greet('voice')
                self.wait_for_speech()
        else:
            self.wait_for_input'''
        

    def speak(self, output): 
        global num 
    
        # num to rename every audio file  
        # with different name to remove ambiguity 
        num += 1
        print("PerSon : ", output) 
    
        toSpeak = gTTS(text = output, lang =str(self.lang), slow = False) 
        # saving the audio file given by google text to speech 
        file = str(num)+".mp3"
        toSpeak.save(file) 
        
        # playsound package is used to play the same file. 
        playsound.playsound(file, True)  
        os.remove(file) 

    def greet(self, mode):
        if mode=='text':
            print('Olá, sou seu assistente virtual, como posso te ajudar hoje?')
        else:
            self.speak("Olá, sou seu assistente virtual, como posso te ajudar hoje?")


    def wait_for_speech(self):
        while True:
            order=str(input())
            return
    '''testing methods only, this will be moved to bridge.py
        once i figure out a decent way to isolate terms'''
    def dicio(self, word):
        speech=define(word)
        self.speak(speech)

    def hour(self):
        time=now()
        self.speak(time)

    def twitter(self, text, img):
        tweet(text, img)
        self.speak(f'tweetando: {text}')
            
