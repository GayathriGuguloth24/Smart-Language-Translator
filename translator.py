from langdetect import detect
from deep_translator import GoogleTranslator

def detect_language(text):
    return detect(text)

def translate_text(text, target_language):
    translated=GoogleTranslator(
        source="auto",
        target=target_language
    ).translate(text)

    return translated

text=input("Enter text: ")

detecte_language=detect_language(text)

print("Detected Language:", 
detect_language)

target_language= input("Enter target language code: ")

translate_text=translate_text(text,target_language)

print("Translated text:" , translate_text)
