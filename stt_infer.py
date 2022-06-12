import stt
from stt import Model
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
    
    
    dsSTT = Model('./stt_models/sinhala_model_v0.1.0.tflite')
    #dsSTT = Model('./stt_models/eng_model.tflite')
    
    dsSTT.enableExternalScorer('./stt_models/Scorer/kenlm-medium-sinhala.scorer')
    #dsSTT.enableExternalScorer('./stt_models/Scorer/huge-vocabulary.scorer')

    #dsSTT.setBeamWidth(10)
    #dsSTT.beamWidth()

    #dsSTT.addHotWord()

    fs, audio = wav.read(audio_file)
    generated_words = dsSTT.stt(audio)

    #dsSTT.sttWithMetadata(audio, 2)

    #tra = stt.CandidateTranscript()
    #print(tra.tokens())

    count_time,count_delay,total_words=0,0,0
    words_list=[]
    total_words = len(generated_words)
    print('Total Recognised Words:', total_words)
    """for i,words_full in enumerate(generated_words):
        words_list.append(generated_words[i]['word'])
        #count_time=count_time+float(generated_words[i]['duration'])
        if i != len(generated_words)-1:
            #print(len(generated_words))
            count_delay=count_delay+abs((generated_words[i]['start_time ']+generated_words[i]['duration']-generated_words[i+1]['start_time '])) """
    #total_time=round(count_time+count_delay,3)
    #print('total time for words:',round(count_time+count_delay,3))
    """if total_words==0:
        print("words per minute: 0 \n Not Recognised")
        wpm=0
    else:
        print('words per minute:',round((60/total_time)*total_words))
        wpm=(60/total_time)*total_words"""
    #aigalore_filler_words=[]
    #aigalore_filler_words.append(' '.join(token.lower() for token in nltk.word_tokenize(text) if token.lower() not in stopwords.words('english')))

    #print(len(str(text)),len(str(aigalore_filler_words[0])))
    #total_filler_words=len(word_tokenize(text))-len(word_tokenize(str(aigalore_filler_words[0])))
    #text = text + "<br><br>" + "<b>Total Recognised Words:</b>" + str(total_words) + '<br>' + '<b>Words Per Minute:</b>' +str(wpm)+'<br>'+'<b>Total Filler Words:</b>'+str(total_filler_words)
    #text = text + "<br><br>" + "<b>Total Recognised Words:</b>" + str(total_words) + '<br>' + '<b>Words Per Minute:</b>' + '<br>'+'<b>Total Filler Words:</b>'+str(total_filler_words)

    #print('total filler words:',total_filler_words)
    with open("Files/Transcript/output.txt", "w+") as f:
        f.write(generated_words)
    
    return(generated_words)

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
