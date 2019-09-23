
import speech_recognition as sr 
import time

from PyQt5.QtWidgets import QMessageBox

import playsound
import voiceAssistant
counter = 0;

lang_name = "fa-IR"

class Speech:

    def SpeechFunc(self) :

        sample_rate = 48000
        chunk_size = 2048
        r = sr.Recognizer() 

        mic_list = sr.Microphone.list_microphone_names()
              
        global text

        try:
            micro_name
        except NameError:
            self.SetMicName( mic_list[0])
            
        for i, microphone_name in enumerate(mic_list): 
            if microphone_name == self.getMic():
                device_id = i 

        try:
            with sr.Microphone(device_index = device_id, sample_rate = sample_rate,  
                                    chunk_size = chunk_size) as source: 
                while 1 :
    
                    r.adjust_for_ambient_noise(source) 
                    audio = r.listen(source) 
                    try:    
                        text = r.recognize_google(audio,language=lang_name)
                    except sr.UnknownValueError: 
                    
                        text = "error : سیستم تشخیص صدا نمی تواند صدا را تشخیص دهد دوباره امتحان کنید."
                    
                    except sr.RequestError as e:
                        
                            text = "error :ارتباط با اینترنت  امکان پذیر نیست"
                            
                            
#                             playsound.playsound('noInternet.mp3', True)
                                
                            break
                            
                    if "سوفیا" in text:
                        playsound.playsound('here.mp3', True)
                        text = ""
                        audio = r.listen(source)
                        try:
                            text = r.recognize_google(audio,language=lang_name)
                            break
                            
                          
                        except sr.UnknownValueError: 
    
                            text = "error : سیستم تشخیص صدا نمی تواند صدا را تشخیص دهد دوباره امتحان کنید."
                          
                        except sr.RequestError as e:
    
                            text = "error :ارتباط با اینترنت  امکان پذیر نیست" 
        except:
            text = "error : میکروفن را تغییر دهید"

    def textReturn(self):
        self.SpeechFunc()
        return text
    def mic_lists(self):
        mic_list= sr.Microphone.list_microphone_names()
        return mic_list
    def SetMicName(self,name):
        global micro_name
        micro_name = name;
    def setLang(self,lang):
        global lang_name      
        if not lang_name :
           lang_name = "fa-IR" 
        if (lang == 0):
            lang_name = "fa-IR"
        elif (lang == 1):
            lang_name  = "en-US"
        elif (lang == 2):
            lang_name  = "es"
        elif (lang == 3):
            lang_name  = "ar-IQ"
        elif (lang == 4):
            lang_name  = "tr"
    def getMic(self):
        return micro_name
