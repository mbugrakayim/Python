import base64
import tkinter.messagebox
from tkinter import *

window = Tk()
window.title("Secret Notes")
window.maxsize(360, 700)
window.minsize(360, 700)
window.update()

#İmage
img = PhotoImage(file="TopScrt.png")
image_label = Label(window, image=img  , padx=10, pady=10)
image_label.pack()



#Folder title
titleLabel = Label(window, text="Enter Your Title", padx=10, pady=10 , font=("Arial", 10 , "bold"))
titleEntry = Entry(window)
titleLabel.pack()
titleEntry.pack()

#Note
noteLabel = Label(window, text="Enter Your secret", padx=10, pady=10 , font=("Arial", 10 , "bold"))
noteText = Text(window , width=30 , height=20)
noteLabel.pack()
noteText.pack()

#Master Key
masterKeyLabel = Label(window, text="Enter master key" , padx=10, pady=10 , font=("Arial", 10 , "bold"))
masterKeyEntry = Entry(window)
masterKeyLabel.pack()
masterKeyEntry.pack()

#Button

def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)

def saveAndEncrypt():
    _title = titleEntry.get()
    _note = noteText.get("1.0", END)
    _key = masterKeyEntry.get()
    if _title != "" or len(_note) != 1 or len(_key) != 0:
            msg_encryp = encode(_key, _note)
            try:
                with open("secret.txt","a") as file:
                    file.write(f"\n{_title}\n{msg_encryp}")
            except FileNotFoundError:
                with open(f"secret.txt","w") as file:
                    file.write(f"\n{_title}\n{msg_encryp}")
            finally:
                titleEntry.delete(0, END)
                noteText.delete("1.0", END)
                masterKeyEntry.delete(0, END)

    else:
        tkinter.messagebox.showinfo("Error", "Lütfen İçeriği Giriniz...")

saveButton = Button(window, text="Save & Encrypt" ,command=saveAndEncrypt )
saveButton.pack(padx=10, pady=10)

#Decrypt button
def decrypt_Button():
    _msg = noteText.get("1.0", END)
    _key = masterKeyEntry.get()

    if len(_msg) == 0 or len(_key) == 0:
        tkinter.messagebox.showinfo(title="Error!", message="Please enter all information.")
    else:
        try:
            decrypted_message = decode(_key, _msg)
            noteText.delete("1.0", END)
            noteText.insert("1.0", decrypted_message)
        except:
            tkinter.messagebox.showinfo(title="Error!", message="Please make sure of encrypted info.")



decryptButton = Button(window, text="Decrypt" ,command=decrypt_Button )
decryptButton.pack()


window.mainloop()