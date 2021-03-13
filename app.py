from googletrans import Translator
from text_to_speech import speak


chosen_word_or_phrase = input('Which word or phrase do you want to translate? -> ')

""" e.g. text_to_translate.x where x is the following:
src: The source language
dest: Destination language, which is set to English (en)
origin: Original text, that is 'Mitä sinä teet' in our example
text: Translated text, that will be 'what are you doing?' in our case
pronunciation: Pronunciation of the translated text"""
def translate_text(text):
    translator = Translator()
    text_to_translate = translator.translate(text, dest='pa')
    print('Punjabi: '+ text_to_translate.pronunciation)
    return text_to_translate.pronunciation


# text to audio
def text_to_speech_audio(getText):
    speak(getText, lang='hi')

# translate_text(chosen_word_or_phrase)
text_to_speech_audio(translate_text(chosen_word_or_phrase))


