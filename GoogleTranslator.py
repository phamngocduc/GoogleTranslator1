
from googletrans import Translator
translator = Translator()
translated = translator.translate('I come from England', src='en', dest='vi')
print(translated.text)