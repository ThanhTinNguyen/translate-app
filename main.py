import tkinter
from tkinter import *
from calendar import c
import googletrans
from googletrans import Translator
#print(googletrans.LANGUAGES)
# define a translate object
translator = Translator()
a=translator.detect("em dep qua")
translation = translator.translate("Der Himmel ist blau und ich mag Bananen", dest='vi')
print(a)


root=Tk()
root.title('Google Translate')
root.geometry('800x400')
root.iconbitmap('logo.ico')

names=('vietnamese','english', 'french','chinese (simplified)','chinese (traditional)','japanese','afrikaans','albanian', 'amharic','arabic', 'armenian', 'azerbaijani', 'basque','belarusian','bengali', 'bosnian', 'bulgarian', 'catalan', 'cebuano','chichewa','corsican','croatian','czech','danish','dutch','esperanto','estonian','filipino','finnish','frisian','galician','georgian','german', 'greek', 'gujarati', 'haitian creole', 'hausa', 'hawaiian', 'hebrew', 'hebrew','hindi','hmong','hungarian', 'icelandic', 'igbo', 'indonesian','irish','italian','javanese','kannada','kazakh', 'khmer', 'korean','kurdish (kurmanji)','kyrgyz','lao','latin','latvian','lithuanian','luxembourgish','macedonian','malagasy','malay', 'malayalam', 'maltese','maori','marathi','mongolian','myanmar (burmese)','nepali', 'norwegian','odia','pashto','persian','polish','portuguese','punjabi','romanian','russian','samoan','scots gaelic','serbian','sesotho','shona','sindhi','sinhala','slovak','slovenian','somali','spanish', 'sundanese', 'swahili','swedish','tajik','tamil','telugu','thai', 'turkish','ukrainian','urdu','uyghur','uzbek','welsh','xhosa','yiddish','yoruba','zulu')
myspin=Spinbox(root,values=names,font=('Arial',18))
myspin.pack(pady=10)

output=myspin.get()

languages={'af': 'afrikaans', 'sq': 'albanian', 'am': 'amharic', 'ar': 'arabic', 'hy': 'armenian', 'az': 'azerbaijani', 'eu': 'basque', 'be': 'belarusian', 'bn': 'bengali', 'bs': 'bosnian', 'bg': 'bulgarian', 'ca': 'catalan', 'ceb': 'cebuano', 'ny': 'chichewa', 'zh-cn': 'chinese (simplified)', 'zh-tw': 'chinese (traditional)', 'co': 'corsican', 'hr': 'croatian', 'cs': 'czech', 'da': 'danish', 'nl': 'dutch', 'en': 'english', 'eo': 'esperanto', 'et': 'estonian', 'tl': 'filipino', 'fi': 'finnish', 'fr': 'french', 'fy': 'frisian', 'gl': 'galician', 'ka': 'georgian', 'de': 'german', 'el': 'greek', 'gu': 'gujarati', 'ht': 'haitian creole', 'ha': 'hausa', 'haw': 'hawaiian', 'iw': 'hebrew', 'he': 'hebrew', 'hi': 'hindi', 'hmn': 'hmong', 'hu': 'hungarian', 'is': 'icelandic', 'ig': 'igbo', 'id': 'indonesian', 'ga': 'irish', 'it': 'italian', 'ja': 'japanese', 'jw': 'javanese', 'kn': 'kannada', 'kk': 'kazakh', 'km': 'khmer', 'ko': 'korean', 'ku': 'kurdish (kurmanji)', 'ky': 'kyrgyz', 'lo': 'lao', 'la': 'latin', 'lv': 'latvian', 'lt': 'lithuanian', 'lb': 'luxembourgish', 'mk': 'macedonian', 'mg': 'malagasy', 'ms': 'malay', 'ml': 'malayalam', 'mt': 'maltese', 'mi': 'maori', 'mr': 'marathi', 'mn': 'mongolian', 'my': 'myanmar (burmese)', 'ne': 'nepali', 'no': 'norwegian', 'or': 'odia', 'ps': 'pashto', 'fa': 'persian', 'pl': 'polish', 'pt': 'portuguese', 'pa': 'punjabi', 'ro': 'romanian', 'ru': 'russian', 'sm': 'samoan', 'gd': 'scots gaelic', 'sr': 'serbian', 'st': 'sesotho', 'sn': 'shona', 'sd': 'sindhi', 'si': 'sinhala', 'sk': 'slovak', 'sl': 'slovenian', 'so': 'somali', 'es': 'spanish', 'su': 'sundanese', 'sw': 'swahili', 'sv': 'swedish', 'tg': 'tajik', 'ta': 'tamil', 'te': 'telugu', 'th': 'thai', 'tr': 'turkish', 'uk': 'ukrainian', 'ur': 'urdu', 'ug': 'uyghur', 'uz': 'uzbek', 'vi': 'vietnamese', 'cy': 'welsh', 'xh': 'xhosa', 'yi': 'yiddish', 'yo': 'yoruba', 'zu': 'zulu'}
for i in languages:
    if languages[i]== output:
        c=i
print(c)

root.mainloop()
