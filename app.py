from tkinter import *
from PIL import Image,ImageTk
from googletrans import Translator
from win32com.client import Dispatch
from playsound import playsound
from gtts import gTTS
import os

#create Tk window
root=Tk()
root.title('Google Translate')
root.geometry('800x400')
root.iconbitmap('logo.ico')

#Load background
load=Image.open('12.png')
render=ImageTk.PhotoImage(load)
img=Label(root,image= render)
img.place(x=0,y=-93)

#Headings
name=Label(root,text='Translator',fg='#FFFFFF',bd=0,bg='#8694c8')
name.config(font=('Transformers Movie',40))
name.place(x=250,y=10)

#input box
box=Text(root,width=58,height=4,font=('ROBOTO',16))
box.place(x=50,y=85)

#ouput box
box1=Text(root,width=58,height=4,font=('ROBOTO',16))
box1.place(x=50,y=250)

#button
button_frame=Frame(root).pack(side=BOTTOM)

#speaker
speaker = Dispatch('SAPI.spVoice')

#choose OUPUT languages
names=('vietnamese','english', 'french','chinese (simplified)','chinese (traditional)','japanese','afrikaans','albanian', 'amharic','arabic', 'armenian', 'azerbaijani', 'basque','belarusian','bengali', 'bosnian', 'bulgarian', 'catalan', 'cebuano','chichewa','corsican','croatian','czech','danish','dutch','esperanto','estonian','filipino','finnish','frisian','galician','georgian','german', 'greek', 'gujarati', 'haitian creole', 'hausa', 'hawaiian', 'hebrew', 'hebrew','hindi','hmong','hungarian', 'icelandic', 'igbo', 'indonesian','irish','italian','javanese','kannada','kazakh', 'khmer', 'korean','kurdish (kurmanji)','kyrgyz','lao','latin','latvian','lithuanian','luxembourgish','macedonian','malagasy','malay', 'malayalam', 'maltese','maori','marathi','mongolian','myanmar (burmese)','nepali', 'norwegian','odia','pashto','persian','polish','portuguese','punjabi','romanian','russian','samoan','scots gaelic','serbian','sesotho','shona','sindhi','sinhala','slovak','slovenian','somali','spanish', 'sundanese', 'swahili','swedish','tajik','tamil','telugu','thai', 'turkish','ukrainian','urdu','uyghur','uzbek','welsh','xhosa','yiddish','yoruba','zulu')
myspin=Spinbox(root,values=names,font=('Arial',18))
myspin.place(x=50,y=200)

#function Clear_text:
def clear():
    box.delete(1.0,END)
    box1.delete(1.0,END)

#function Translate:
def translate():
    box1.delete(1.0,END)

    #get INPUT
    INPUT=box.get(1.0,END)
    #print(INPUT)

    #get OUTPUT
    output=myspin.get()

    languages={'af': 'afrikaans', 'sq': 'albanian', 'am': 'amharic', 'ar': 'arabic', 'hy': 'armenian', 'az': 'azerbaijani', 'eu': 'basque', 'be': 'belarusian', 'bn': 'bengali', 'bs': 'bosnian', 'bg': 'bulgarian', 'ca': 'catalan', 'ceb': 'cebuano', 'ny': 'chichewa', 'zh-cn': 'chinese (simplified)', 'zh-tw': 'chinese (traditional)', 'co': 'corsican', 'hr': 'croatian', 'cs': 'czech', 'da': 'danish', 'nl': 'dutch', 'en': 'english', 'eo': 'esperanto', 'et': 'estonian', 'tl': 'filipino', 'fi': 'finnish', 'fr': 'french', 'fy': 'frisian', 'gl': 'galician', 'ka': 'georgian', 'de': 'german', 'el': 'greek', 'gu': 'gujarati', 'ht': 'haitian creole', 'ha': 'hausa', 'haw': 'hawaiian', 'iw': 'hebrew', 'he': 'hebrew', 'hi': 'hindi', 'hmn': 'hmong', 'hu': 'hungarian', 'is': 'icelandic', 'ig': 'igbo', 'id': 'indonesian', 'ga': 'irish', 'it': 'italian', 'ja': 'japanese', 'jw': 'javanese', 'kn': 'kannada', 'kk': 'kazakh', 'km': 'khmer', 'ko': 'korean', 'ku': 'kurdish (kurmanji)', 'ky': 'kyrgyz', 'lo': 'lao', 'la': 'latin', 'lv': 'latvian', 'lt': 'lithuanian', 'lb': 'luxembourgish', 'mk': 'macedonian', 'mg': 'malagasy', 'ms': 'malay', 'ml': 'malayalam', 'mt': 'maltese', 'mi': 'maori', 'mr': 'marathi', 'mn': 'mongolian', 'my': 'myanmar (burmese)', 'ne': 'nepali', 'no': 'norwegian', 'or': 'odia', 'ps': 'pashto', 'fa': 'persian', 'pl': 'polish', 'pt': 'portuguese', 'pa': 'punjabi', 'ro': 'romanian', 'ru': 'russian', 'sm': 'samoan', 'gd': 'scots gaelic', 'sr': 'serbian', 'st': 'sesotho', 'sn': 'shona', 'sd': 'sindhi', 'si': 'sinhala', 'sk': 'slovak', 'sl': 'slovenian', 'so': 'somali', 'es': 'spanish', 'su': 'sundanese', 'sw': 'swahili', 'sv': 'swedish', 'tg': 'tajik', 'ta': 'tamil', 'te': 'telugu', 'th': 'thai', 'tr': 'turkish', 'uk': 'ukrainian', 'ur': 'urdu', 'ug': 'uyghur', 'uz': 'uzbek', 'vi': 'vietnamese', 'cy': 'welsh', 'xh': 'xhosa', 'yi': 'yiddish', 'yo': 'yoruba', 'zu': 'zulu'}
    for i in languages:
        if languages[i]== output:
            c=i
    #translate code
    translator = Translator()
    a = translator.translate(INPUT, dest=c)
    b=a.text
    #export to output box
    box1.insert(END,b)

def play_sound():
    #get INPUT
    INPUT=box.get(1.0,END)
    #get OUTPUT
    output=myspin.get()

    languages={'af': 'afrikaans', 'sq': 'albanian', 'am': 'amharic', 'ar': 'arabic', 'hy': 'armenian', 'az': 'azerbaijani', 'eu': 'basque', 'be': 'belarusian', 'bn': 'bengali', 'bs': 'bosnian', 'bg': 'bulgarian', 'ca': 'catalan', 'ceb': 'cebuano', 'ny': 'chichewa', 'zh-cn': 'chinese (simplified)', 'zh-tw': 'chinese (traditional)', 'co': 'corsican', 'hr': 'croatian', 'cs': 'czech', 'da': 'danish', 'nl': 'dutch', 'en': 'english', 'eo': 'esperanto', 'et': 'estonian', 'tl': 'filipino', 'fi': 'finnish', 'fr': 'french', 'fy': 'frisian', 'gl': 'galician', 'ka': 'georgian', 'de': 'german', 'el': 'greek', 'gu': 'gujarati', 'ht': 'haitian creole', 'ha': 'hausa', 'haw': 'hawaiian', 'iw': 'hebrew', 'he': 'hebrew', 'hi': 'hindi', 'hmn': 'hmong', 'hu': 'hungarian', 'is': 'icelandic', 'ig': 'igbo', 'id': 'indonesian', 'ga': 'irish', 'it': 'italian', 'ja': 'japanese', 'jw': 'javanese', 'kn': 'kannada', 'kk': 'kazakh', 'km': 'khmer', 'ko': 'korean', 'ku': 'kurdish (kurmanji)', 'ky': 'kyrgyz', 'lo': 'lao', 'la': 'latin', 'lv': 'latvian', 'lt': 'lithuanian', 'lb': 'luxembourgish', 'mk': 'macedonian', 'mg': 'malagasy', 'ms': 'malay', 'ml': 'malayalam', 'mt': 'maltese', 'mi': 'maori', 'mr': 'marathi', 'mn': 'mongolian', 'my': 'myanmar (burmese)', 'ne': 'nepali', 'no': 'norwegian', 'or': 'odia', 'ps': 'pashto', 'fa': 'persian', 'pl': 'polish', 'pt': 'portuguese', 'pa': 'punjabi', 'ro': 'romanian', 'ru': 'russian', 'sm': 'samoan', 'gd': 'scots gaelic', 'sr': 'serbian', 'st': 'sesotho', 'sn': 'shona', 'sd': 'sindhi', 'si': 'sinhala', 'sk': 'slovak', 'sl': 'slovenian', 'so': 'somali', 'es': 'spanish', 'su': 'sundanese', 'sw': 'swahili', 'sv': 'swedish', 'tg': 'tajik', 'ta': 'tamil', 'te': 'telugu', 'th': 'thai', 'tr': 'turkish', 'uk': 'ukrainian', 'ur': 'urdu', 'ug': 'uyghur', 'uz': 'uzbek', 'vi': 'vietnamese', 'cy': 'welsh', 'xh': 'xhosa', 'yi': 'yiddish', 'yo': 'yoruba', 'zu': 'zulu'}
    for i in languages:
        if languages[i]== output:
            c=i
    #translate code
    translator = Translator()
    a = translator.translate(INPUT, dest=c)
    b=a.text

    speak = gTTS(text=b, lang=c, slow=False)
    speak.save('captured_voice.mp3')
    playsound('captured_voice.mp3')
    os.remove('captured_voice.mp3')

#sound button
#icon = PhotoImage(file='speaker01.png')
#sound_btn = Button(button_frame, image=icon, width=30,height=30,bg='#FFFFFF',bd=0,command=play_sound)
#sound_btn.place(x=715,y=90)

icon1 = PhotoImage(file='speaker01.png')
sound_btn1 = Button(button_frame, image=icon1, width=30,height=30,bg='#FFFFFF',bd=0,command=play_sound)
sound_btn1.place(x=715,y=255)


#clear text button & translate button
clear_button=Button(button_frame,text='Clear text',font=(('Arial'),10,'bold'),bg='#38b000',fg='#FFFFFF',command=clear)
clear_button.place(x=450,y=200)
trans_button=Button(button_frame,text='Translate',font=(('Arial'),10,'bold'),bg='#38b000',fg='#FFFFFF',command=translate)
trans_button.place(x=350,y=200)

root.mainloop()