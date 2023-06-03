from translator import englishToFrench
from translator import frenchToEnglish

english_word = input("Enter an English word: ")
french_translation = englishToFrench(english_word)
print(f"The French translation of '{english_word}' is '{french_translation}'.")

french_word = input("Enter an french word: ")
english_translation = frenchToEnglish(french_word)
print(f"The French translation of '{french_word}' is '{english_translation}'.")
