import os
from multiprocess import Process
from threading import Thread

import playsound
from gtts import gTTS

from speech2text.main import record



num = 1
class Cortana:
    def __init__(self, *lang, **kw):
        if lang:
            self.lang=lang[0]
        else:
            self.lang='pt'
        #mode
        self.wait()

    def speak(self, output): 
        global num 
    
        # num to rename every audio file  
        # with different name to remove ambiguity 
        num += 1
        print("Cortana : ", output) 
    
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
        elif mode=='voice':
            self.speak("Olá, sou seu assistente virtual, como posso te ajudar hoje?")
        self.wait()


    def wait(self):
        global switch
        switch=True
        def wait_speech():
            speech=record()
            if 'cortana' in speech.lower():
                self.greet('voice')
                return
        
        def wait_input():
            while True:
                text=input()
                if 'cortana' in text.lower():
                    self.greet('text')
                    break
            return

        x=Process(target=wait_speech) 
        x.start()
        wait_input()
        #sync(x,y)
        


    def recognize(self):
        print('recognizing speech/words')
        pass
