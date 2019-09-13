
import speech_recognition as sr 
# from threading import Thread
# from multiprocessing.pool import ThreadPool
import time

from PyQt5.QtWidgets import QMessageBox

lang_name = "fa-IR"

class Speech:

    def SpeechFunc(self) :
        #enter the name of usb microphone that you found 
        #using lsusb 
        #the following name is only used as an example 
        
#         mic_name = "Jack-Mic (High Definition Audio"

        #Sample rate is how often values are recorded 
        sample_rate = 48000
        #Chunk is like a buffer. It stores 2048 samples (bytes of data) 
        #here.  
        #it is advisable to use powers of 2 such as 1024 or 2048 
        chunk_size = 2048
        #Initialize the recognizer 
        r = sr.Recognizer() 
          
#         r.pause_threshold = 1.0
#         r.phrase_threshold = 1.0
#         r.non_speaking_duration = 0.3
        
        #generate a list of all audio cards/microphones 
#         micro_name = "default"

        mic_list = sr.Microphone.list_microphone_names()
#         for m in mic_list:
              
        global text
#         if  micro_name == "default" :
#             micro_name = mic_list[1]
        try:
            micro_name
        except NameError:
            self.SetMicName( mic_list[0])

        #the following loop aims to set the device ID of the mic that 
        #we specifically want to use to avoid ambiguity.
#         print(self.getMic())
        for i, microphone_name in enumerate(mic_list): 
            if microphone_name == self.getMic():
                device_id = i 


        
          
        #use the microphone as source for input. Here, we also specify  
        #which device ID to specifically look for incase the microphone  
        #is not working, an error will pop up saying "device_id undefined" 
        
        with sr.Microphone(device_index = device_id, sample_rate = sample_rate,  
                                chunk_size = chunk_size) as source: 
            #wait for a second to let the recognizer adjust the  
            #energy threshold based on the surrounding noise level 
            r.adjust_for_ambient_noise(source) 
#             print ("Say Something")
            #listens for the user's input 
            audio = r.listen(source) 
    
            try:
#                 time.sleep(10) 
                
                text = r.recognize_google(audio,language=lang_name)
                
#                 return text
#                 print ("you said: " + str(text.encode("utf-8"))) 
              
            #error occurs when google could not understand what was said 
              
            except sr.UnknownValueError: 
#                 text = "error : Google Speech Recognition could not understand audio"
                text = "error : سیستم تشخیص صدا نمی تواند صدا را تشخیص دهد دوباره امتحان کنید."
#                 print("Google Speech Recognition could not understand audio") 
              
            except sr.RequestError as e:
#                 text = "error : Could not request results from Google Speech Recognition service; {0}".format(e) 
                text = "error :ارتباط با اینترنت  امکان پذیر نیست" 
#                 print("Could not request results from Google Speech Recognition service; {0}".format(e)) 
#     def threadFunc(self):
#         pool = ThreadPool(processes=1)
#         
#         async_result = pool.apply_async(self.SpeechFunc()) # tuple of args for foo
#         
#         # do some other stuff in the main process
#         
#         return_val = async_result.get()
#         return return_val
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
