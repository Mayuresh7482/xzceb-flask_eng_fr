from deep_translator import MyMemoryTranslator


def englishToFrench(english_text):
    """
    Translates English text to French using MyMemoryTranslator.
    Args:
        english_text (str): The English text to be translated.
    Returns:
        str: The translated French text.
    """
    translator = MyMemoryTranslator(source='en', target='fr')
    french_text = translator.translate(english_text)
    return french_text


def frenchToEnglish(french_text):
    """
    Translates French text to English using MyMemoryTranslator.
    Args:
        french_text (str): The French text to be translated.
    Returns:
        str: The translated English text.
    """
    translator = MyMemoryTranslator(source='fr', target='en')
    english_text = translator.translate(french_text)
    return english_text


def translate_english_to_french():
    english_text = input("Enter an English word or phrase: ")
    french_translation = englishToFrench(english_text)
    print(f"The French translation of '{english_text}' is '{french_translation}'.")


def translate_french_to_english():
    french_text = input("Enter a French word or phrase: ")
    english_translation = frenchToEnglish(french_text)
    print(f"The English translation of '{french_text}' is '{english_translation}'.")


if __name__ == '__main__':
    translate_english_to_french()
    translate_french_to_english()
