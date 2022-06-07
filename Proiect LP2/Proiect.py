from tkinter import *
import requests
import os.path
import plotly.express as px

file_exists = os.path.exists('downloaded.csv')
if file_exists == 0:
    url = 'https://data.primariatm.ro/dataset/b19f4ada-7031-4ac9-b627-6a73c6dd960a/resource/43caecf1-5990-4f3d-84f8-0aefae43fdf0/download/telecomuncaii.csv'
    req = requests.get(url)
    url_content = req.content
    csv_file = open('downloaded.csv', 'wb')
    csv_file.write(url_content)
    csv_file.close()
lines = []
a = 0
b = ''
list = []
lista_mare = []
with open('downloaded.csv', 'r') as f:
    for line in f:
        for i in range(len(line)):
            if line[i] == ',':
                i = i + 1
                while line[i] != ',':
                    a = a * 10 + int(line[i])
                    i = i + 1
                    if i == len(line) - 1:
                        break
                list.append(a)
                a = 0
        lista_mare.append(list)
        list = []
# interfata grafica
root = Tk()
root.geometry('800x500')
root.title('Telecomunicatii')
root['bg']='#5d8a82'
categorii = (('Număr conexiuni de acces la internet furnizate la puncte fixe - total'),
             ('Număr conexiuni de acces la internet furnizate la puncte fixe - persoane fizice'),
             ('Număr conexiuni de acces la internet furnizate la puncte fixe - persoane juridice'))

label = Label(text="Alegeti una din categoriile de mai jos:",font=("time", 14))
label.pack(fill='x', padx=5, pady=5)

var = IntVar()
# radio buttons
def activate_submit():
    if var.get()>=1:
        button['state']=NORMAL
    elif var.get()==0:
        button['state']=DISABLED
    else:
        print('something went wrong!')
for i in range(0,len(categorii)):
    r = Radiobutton(root, text=categorii[i],command=activate_submit,variable=var, value=i+1,bg='#5d8a82',font=("time", 12)).pack(anchor=W)

def afisare():
    n = var.get()
    df = px.data.tips()
    fig = px.line(x=lista_mare[0], y=lista_mare[n])
    fig.update_layout(xaxis_title='Ani', yaxis_title='Numar Conexiuni')
    fig.show()

# buton de afisare
button = Button(root, text="Genereaza grafic",bg='#345', fg='white', activebackground="black", activeforeground="white",state=DISABLED,relief=RAISED, command=afisare, font="Raleway")



button.pack(fill='x', padx=100, pady=20)

root.mainloop()
