#import stt 
#from stt import Model
import speech_recognition as sr
import wave
import scipy.io.wavfile as wav 
import nltk
import numpy as np
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
#nltk.download('punkt')
#nltk.download('stopwords') 

nltk.data.path.append('./nltk_data')

def func(audio_file, transcript):
    print(audio_file)
     
    r = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = r.record(source)

    message = r.recognize_google(audio, language="si-LK")
    print(message)    
    
    return(message)

def words_from_metadata(metadata):
    word = ""
    word_list = []
    word_start_time = 0
    # Loop through each character
    for i in range(0, metadata.num_items):
        item = metadata.items[i]
        # Append character to word if it's not a space
        if item.character != " ":
            word = word + item.character
        # Word boundary is either a space or the last character in the array
        if item.character == " " or i == metadata.num_items - 1:
            word_duration = item.start_time - word_start_time

            if word_duration < 0:
                word_duration = 0

            each_word = dict()
            each_word["word"] = word
            each_word["start_time "] = round(word_start_time, 4)
            each_word["duration"] = round(word_duration, 4)

            word_list.append(each_word)
            # Reset
            word = ""
            word_start_time = 0
        else:
            if len(word) == 1:
                # Log the start time of the new word
                word_start_time = item.start_time

    return word_list
##ddd