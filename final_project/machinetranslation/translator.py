"""
Complex of functions that translates passed as argument text 
"""
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """
    Return French text translated from provided English text 
    """
    french_text = MyMemoryTranslator(source='en-GB', target='fr-FR').translate(english_text)
    return french_text

def french_to_english(french_text):
    """
    Return English text translated from provided French text 
    """
    english_text = MyMemoryTranslator(source='fr-FR', target='en-GB').translate(french_text)
    return english_text
