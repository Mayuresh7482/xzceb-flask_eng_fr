from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    #write the code here
    """
    This function returns the traduction of english text to french
    """
    french_text = MyMemoryTranslator(source='en', target='fr').translate(english_text)
    return french_text

def french_to_english(french_text):
    #write the code here
    """
    This function returns the traduction of french text to english
    """
    english_text= MyMemoryTranslator(source='fr', target='en').translate(french_text)
    return english_text
