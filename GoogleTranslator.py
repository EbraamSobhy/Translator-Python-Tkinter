from tkinter import *
from tkinter import ttk, messagebox
import googletrans
import textblob
from textblob import TextBlob
from langdetect import detect, DetectorFactory
from googletrans import Translator, LANGUAGES

root = Tk()
root.title("Google Translator")
root.geometry("1080x400")

# Functions label_change
def label_change():
    c = combo1.get()
    c1 = combo2.get()
    label1.configure(text=c)
    label2.configure(text=c1)
    root.after(1000, label_change)
    
# Ensure consistent language detection results
DetectorFactory.seed = 0

# Define your language dictionary if not already defined
language = {
    'en': 'English',
    'es': 'Spanish',
    'fr': 'French',
    # Add other languages as needed
}

translator = Translator()

def translate_now():
    global language
    try:
        text_ = text1.get(1.0, 'end-1c')  # Use 'end-1c' to avoid including the newline character
        c2 = combo1.get()
        c3 = combo2.get()
        
        if text_:
            # Detect language using langdetect
            lan = detect(text_)
            lan_ = None
            
            # Find the language code from the language dictionary
            for i, j in language.items():
                if j == c3:
                    lan_ = i
                    break
            
            if lan_:
                # Perform translation
                translated = translator.translate(text_, src=lan, dest=lan_)
                text2.delete(1.0, 'end')
                text2.insert('end', translated.text)
            else:
                messagebox.showerror("Translation Error", "Target language not found in dictionary.")
        else:
            messagebox.showwarning("Input Error", "No text provided to translate.")
            
    except Exception as e:
        messagebox.showerror("Translation Error", f"An error occurred: {str(e)}")

# Icon
image_icon = PhotoImage(file="google.png")
root.iconphoto(False, image_icon)

# arrow
arrow_image = PhotoImage(file="arrow.png")
image_label = Label(root, image=arrow_image, width=150)
image_label.place(x = 460, y = 50)

# Language Setup
language = googletrans.LANGUAGES
languageV = list(language.values())
lang1 = language.keys()

combo1 = ttk.Combobox(root, values=languageV, font="Roboto 14", state="readonly")
combo1.place(x=110, y=20)
combo1.set("ENGLISH")

label1 = Label(root, text="ENGLISH", font="saga 30 bold", bg="white", width=18, bd=5, relief=GROOVE)
label1.place(x=10, y=50)

f = Frame(root, bg="Black", bd=5)
f.place(x=10, y=118, width=440, height=210)
text1 = Text(f, font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=430, height=200)

Scrollbar1 = Scrollbar(f)
Scrollbar1.pack(side="right", fill="y")
Scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=Scrollbar1.set)

combo2 = ttk.Combobox(root, values=languageV, font="Roboto 14", state="readonly")
combo2.place(x=730, y=20)
combo2.set("SELECT LANGUAGE")

label2 = Label(root, text="ENGLISH", font="saga 30 bold", bg="white", width=18, bd=5, relief=GROOVE)
label2.place(x=620, y=50)

f1 = Frame(root, bg="Black", bd=5)
f1.place(x=620, y=118, width=440, height=210)
text2 = Text(f1, font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD)
text2.place(x=0, y=0, width=430, height=200)

Scrollbar2 = Scrollbar(f1)
Scrollbar2.pack(side="right", fill="y")
Scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=Scrollbar2.set)

# Translate Button
translate = Button(root, text="Translate", font="Roboto 15 bold italic",
                    activebackground = "green", cursor = "hand2", bd = 5, bg = "red", fg = "white", command=translate_now)
translate.place(x = 480, y = 260)

label_change()

root.configure(bg="white")
root.mainloop()