from tkinter import *
import random
import string

def generatePass():
    lst=[]
    for i in range(1,13):
        alphabet_lower=list(string.ascii_lowercase)
        alphabet_upperr=list(string.ascii_uppercase)
        alphabet_symbols=list(string.punctuation)
        str=alphabet_lower+alphabet_upperr+alphabet_symbols
        character=random.choice(str)
        lst.append(character)
    a="".join(lst)
    print=(a)
    label.config(text=a)
    
root = Tk()
root.title("Generador de password")
root.geometry('500x500')
root.resizable(0,0)

my_button=Button(root, text="Generar", font='Georgia 15 bold', command=generatePass).pack()        #de esta forma el boton se hace visible dentro de la ventana
my_label=Label(root, text="").pack()
exit_button=Button(root, text="Salir", font="Georgia 15 bold", command=root.destroy).pack()

label=Label(root,text="", font='Georgia 15 bold')
label_et=Label(root, text="Este es el password : ", font='Georgia 10 bold')
label_et.pack()
label.pack()

root.mainloop()