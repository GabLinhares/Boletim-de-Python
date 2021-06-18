import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as msb
from tkinter import *
import sqlite3

# --------- Frame -------------
root = Tk()
root.title(" Estacio boletim da area python ")
width = 900
height = 600
sc_width = root.winfo_screenwidth()
sc_height = root.winfo_screenheight()
x = (sc_width/2) - (width/2)
y = (sc_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0,0)
root.config(bg='gray')

# --------- Strings -------------

nome  = StringVar()
av1 = StringVar()
av2 = StringVar()
av3 = StringVar()
avd = StringVar()
avds = StringVar()
media = StringVar()
id = None
updateWindow = None
newWindow = None

# --------- Data -------------


def database():
    conn = sqlite3.connect("./work.db")
    cursor = conn.cursor()
    query = """ CREATE TABLE IF NOT EXISTS 'notas' (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome TEXT, av1 TEXT, av2 TEXT, av3 TEXT, avd TEXT, avds TEXT, media TEXT) """
    cursor.execute(query)
    cursor.execute("SELECT * FROM 'notas' ORDER BY nome")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()


def submitData():
    if nome.get() == "" or av1.get() == "" or av2.get() == "" or av3.get() == "" or avd.get() == "" or avds.get() == "" or media.get() == "":
        resultado = msb.showwarning(
            "", "digite '0'na AV3 e AVDS quando não forem necessarios.", icon="warning")

    else:
        tree.delete(*tree.get_children())
        conn = sqlite3.connect("./work.db")
        cursor = conn.cursor()
        query = """ INSERT INTO 'notas' (nome, av1, av2, av3, avd, avds, media) VALUES(?, ?, ?, ?, ?, ?, ?)"""
        cursor.execute(query, (str(nome.get()), str(av1.get()), str(
            av2.get()), str(av3.get()), str(avd.get()), str(avds.get()), str(media.get())))
        conn.commit()
        cursor.execute("SELECT * FROM 'notas' ORDER BY nome")
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()
        nome.set("")
        av1.set("")
        av2.set("")
        av3.set("")
        avd.set("")
        avds.set("")
        media.set("")
        


def updateData():
    tree.delete(*tree.get_children())
    conn = sqlite3.connect("./work.db")
    cursor = conn.cursor()
    cursor.execute(""" UPDATE 'notas' SET nome = ?, av1 = ?, av2 = ?, av3 = ?, avd = ?, avds = ?, media = ? WHERE id = ?""",
                   (str(nome.get()), str(av1.get()), str(av2.get()), str(av3.get()), str(avd.get()), str(avds.get()), str(media.get()), int(id)))
    conn.commit()
    cursor.execute("SELECT * FROM 'notas' ORDER BY nome")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()
    nome.set("")
    av1.set("")
    av2.set("")
    av3.set("")
    avd.set("")
    avds.set("")
    media.set("")
    updateWindow.destroy()


def onSelect(event):
    global id, updateWindow
    selectItem = tree.focus()
    conteudo = (tree.item(selectItem))
    selectedItem = conteudo['values']
    id = selectedItem[0]
    nome.set("")
    av1.set("")
    av2.set("")
    av3.set("")
    avd.set("")
    avds.set("")
    media.set("")

    nome.set(selectedItem[1])
    av1.set(selectedItem[2])
    av2.set(selectedItem[3])
    av3.set(selectedItem[4])
    avd.set(selectedItem[5])
    avds.set(selectedItem[6])
    media.set(selectedItem[7])

    # --------- Frames atualizar -------------
    updateWindow = Toplevel()
    updateWindow.title("    ATUALIZAR NOTAS    ")
    formTitulo = Frame(updateWindow)
    formTitulo.pack(side=TOP)
    formContato = Frame(updateWindow)
    formContato.pack(side=TOP, pady=10)
    width = 400
    height = 300
    sc_width = updateWindow.winfo_screenwidth()
    sc_height = updateWindow.winfo_screenheight()
    x = (sc_width/2) - (width/2)
    y = (sc_height/2) - (height/2)
    updateWindow.geometry("%dx%d+%d+%d" % (width, height, x, y))
    updateWindow.resizable(0, 0)

    # --------- Labels atualizar -------------
    lbl_title = Label(formTitulo, text="Atualizando",
                      font=('arial', 18), bg='gray', width=280)
    lbl_title.pack(fill=X)
    lbl_nome = Label(formContato, text='Matricula', font=('arial', 12))
    lbl_nome.grid(row=0, sticky=W)
    lbl_av1 = Label(formContato, text='AV1', font=('arial', 12))
    lbl_av1.grid(row=1, sticky=W)
    lbl_av2= Label(formContato, text='AV2', font=('arial', 12))
    lbl_av2.grid(row=2, sticky=W)
    lbl_av3 = Label(formContato, text='AV3', font=('arial', 12))
    lbl_av3.grid(row=3, sticky=W)
    lbl_avd = Label(formContato, text='AVD', font=('arial', 12))
    lbl_avd.grid(row=4, sticky=W)
    lbl_avds = Label(formContato, text='AVDS', font=('arial', 12))
    lbl_avds.grid(row=5, sticky=W)
    lbl_media = Label(formContato, text='Media', font=('arial', 12))
    lbl_media.grid(row=6, sticky=W)


    # --------- Entrada atualizar -------------
    nomeEntry = Entry(formContato, textvariable=nome, font=('arial', 12))
    nomeEntry.grid(row=0, column=1)
    av1Entry = Entry(formContato, textvariable=av1, font=('arial', 12))
    av1Entry.grid(row=1, column=1)
    av2Entry = Entry(formContato, textvariable=av2, font=('arial', 12))
    av2Entry.grid(row=2, column=1)
    av3Entry = Entry(formContato, textvariable=av3, font=('arial', 12))
    av3Entry.grid(row=3, column=1)
    avdEntry = Entry(formContato, textvariable=avd, font=('arial', 12))
    avdEntry.grid(row=4, column=1)
    avdsEntry = Entry(formContato, textvariable=avds, font=('arial', 12))
    avdsEntry.grid(row=5, column=1)
    mediaEntry = Entry(formContato, textvariable=media, font=('arial', 12))
    mediaEntry.grid(row=6, column=1)
  
    # --------- Botão atualizar -------------
    bttn_updatecom = Button(formContato, text="Atualizar",
                            width=50, command=updateData)
    bttn_updatecom.grid(row=7, columnspan=2, pady=10)


# --------- Deletar -------------
def deleteData():
    if not tree.selection():
        resultado = msb.showwarning(
            '', 'Por favor, selecione o item na lista.', icon='warning')
    else:
        resultado = msb.askquestion(
            '', 'Tem certeza que deseja deletar esse boletim?')
        if resultado == 'yes':
            selectItem = tree.focus()
            conteudo = (tree.item(selectItem))
            selectedItem = conteudo['values']
            tree.delete(selectItem)
            conn = sqlite3.connect("./work.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM 'notas' WHERE id = %d" %
                           selectedItem[0])
            conn.commit()
            cursor.close()
            conn.close()


def insertData():
    global newWindow
    nome.set("")
    av1.set("")
    av2.set("")
    av3.set("")
    avd.set("")
    avds.set("")
    media.set("")

  


    # --------- Frames do cadastro -------------
    newWindow = Toplevel()
    newWindow.title("    INSERINDO NOTAS    ")
    formTitulo = Frame(newWindow)
    formTitulo.pack(side=TOP)
    formContato = Frame(newWindow)
    formContato.pack(side=TOP, pady=10)
    width = 400
    height = 300
    sc_width = newWindow.winfo_screenwidth()
    sc_height = newWindow.winfo_screenheight()
    x = (sc_width/2) - (width/2)
    y = (sc_height/2) - (height/2)
    newWindow.geometry("%dx%d+%d+%d" % (width, height, x, y))
    newWindow.resizable(0, 0)

    # --------- Labels do cadastro -------------
    lbl_title = Label(formTitulo, text="Adicionar nota",
                      font=('arial', 18), bg='gray', width=280)
    lbl_title.pack(fill=X)
    lbl_nome = Label(formContato, text='Matricula', font=('arial', 12))
    lbl_nome.grid(row=0, sticky=W)
    lbl_av1 = Label(formContato, text='Av1', font=('arial', 12))
    lbl_av1.grid(row=1, sticky=W)
    lbl_av2 = Label(formContato, text='Av2', font=('arial', 12))
    lbl_av2.grid(row=2, sticky=W)
    lbl_av3 = Label(formContato, text='Av3', font=('arial', 12))
    lbl_av3.grid(row=3, sticky=W)
    lbl_avd = Label(formContato, text='Avd', font=('arial', 12))
    lbl_avd.grid(row=4, sticky=W)
    lbl_avds = Label(formContato, text='Avds', font=('arial', 12))
    lbl_avds.grid(row=5, sticky=W)
    lbl_media = Label(formContato, text='Media', font=('arial', 12))
    lbl_media.grid(row=6, sticky=W)

    # --------- Entrada de cadastro -------------
    nomeEntry = Entry(formContato, textvariable=nome, font=('arial', 12))
    nomeEntry.grid(row=0, column=1)
    av1Entry = Entry(
        formContato, textvariable=av1, font=('arial', 12))
    av1Entry.grid(row=1, column=1)
    av2Entry = Entry(formContato, textvariable=av2, font=('arial', 12))
    av2Entry.grid(row=2, column=1)
    av3Entry = Entry(formContato, textvariable=av3, font=('arial', 12))
    av3Entry.grid(row=3, column=1)
    avdEntry = Entry(formContato, textvariable=avd, font=('arial', 12))
    avdEntry.grid(row=4, column=1)
    avdsEntry = Entry(formContato, textvariable=avds, font=('arial', 12))
    avdsEntry.grid(row=5, column=1)
    mediaEntry = Entry(formContato, textvariable=media, font=('arial', 12))
    mediaEntry.grid(row=6, column=1)
    # --------- Botão do cadastro -------------
    bttn_submitcom = Button(formContato, text="Exercutar",
                            width=50, command=submitData)
    bttn_submitcom.grid(row=7, columnspan=2, pady=10)


# ---------------- Frame -------------
top = Frame(root, width=500, bd=1, relief=SOLID)
top.pack(side=TOP)
mid = Frame(root, width=500, bg='gray')
mid.pack(side=TOP)
midleft = Frame(mid, width=100)
midleft.pack(side=LEFT, pady=10)
midleftPadding = Frame(mid, width=350, bg="gray")
midleftPadding.pack(side=LEFT)
midright = Frame(mid, width=100)
midright.pack(side=RIGHT, pady=10)
bottom = Frame(root, width=500)
bottom.pack(side=BOTTOM)
tableMargin = Frame(root, width=500)
tableMargin.pack(side=TOP)

# --------------- Label principal --------------
lbl_title = Label(top, text="Boletim de python", font=('arial', 18), width=500)
lbl_title.pack(fill=X)

lbl_alterar = Label(bottom, text="Para alterar clique duas vezes para editar boletim.", font=('arial', 12), width=200)
lbl_alterar.pack(fill=X)

# --------------- Botões principal --------------
bttn_add = Button(midleft, text="INSERIR", bg="white", command=insertData)
bttn_add.pack()
bttn_delete = Button(midright, text="Deletar",
                     bg="Red", command=deleteData)
bttn_delete.pack(side=RIGHT)

# --------------- Treeview --------------

ScrollbarX = Scrollbar(tableMargin, orient=HORIZONTAL)
ScrollbarY = Scrollbar(tableMargin, orient=VERTICAL)

tree = ttk.Treeview(tableMargin, columns=("ID", "Matricula", "AV1", "AV2", "AV3", "AVD", "AVDS", "Media"),
                    height=400, selectmode="extended", yscrollcommand=ScrollbarY.set, xscrollcommand = ScrollbarX.set)
ScrollbarY.config(command=tree.yview)
ScrollbarY.pack(side=RIGHT, fill=Y)
ScrollbarX.config(command=tree.xview)
ScrollbarX.pack(side=BOTTOM, fill=X)
tree.heading("ID", text="ID", anchor=W)
tree.heading("Matricula", text="Matricula", anchor=W)
tree.heading("AV1", text="AV1", anchor=W)
tree.heading("AV2", text="AV2", anchor=W)
tree.heading("AV3", text="AV3", anchor=W)
tree.heading("AVD", text="AVD", anchor=W)
tree.heading("AVDS", text="AVDS", anchor=W)
tree.heading("Media", text="Media", anchor=W)
tree.column('#0', stretch=NO, minwidth=0, width=1)
tree.column('#1', stretch=NO, minwidth=0, width=20)
tree.column('#2', stretch=NO, minwidth=0, width=80)
tree.column('#3', stretch=NO, minwidth=0, width=120)
tree.column('#4', stretch=NO, minwidth=0, width=100)
tree.column('#5', stretch=NO, minwidth=0, width=90)
tree.column('#6', stretch=NO, minwidth=0, width=80)
tree.column('#7', stretch=NO, minwidth=0, width=80)
tree.pack()
tree.bind('<Double-Button-1>', onSelect)

database()
root.mainloop()
