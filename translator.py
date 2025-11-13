from googletrans import Translator

# Create translator object
translator = Translator()

# Input English text
text = input("Enter text in English: ")

# Translate to Spanish
translation = translator.translate(text, src='en', dest='es')

print("Spanish translation:", translation.text)
