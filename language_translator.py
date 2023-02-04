from googletrans import Translator

# Create a Translator object
translator = Translator(service_urls=['translate.google.com'])

# Translate the text
text = "Hello, I am a language translator."
result = translator.translate(text, dest='fr')

# Print the result
print(result.text)
