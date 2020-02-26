import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import messagebox as mBox 

window = tk.Tk()
window.title("EXAMEN DE FINANZAS")

tabControl = ttk.Notebook(window)
tab1 = ttk.Frame(tabControl)

def main():
    pestañitas()

def pestañitas(): 
    tabControl.add(tab1, text = "Examen")
    tabControl.pack(expand = 1, fill = 'both')

def defBoton(tab, text, row, col, comando):
    if tab == 'tab1':
        return ttk.Button(tab1, text = text, command = comando).grid(row = row, column = col)


def llenado1(tab, labelito, row, col, x, y):
    if tab == 'tab1':
        return ttk.Label(tab1, text = labelito).grid(row = row, column = col, padx = 
        x, pady = y)

def chBoton(tab, texto, variable, x ,y, px, py):
    return ttk.Checkbutton(tab1, text = texto, variable = variable).grid(row = x, 
    column = y, padx = px, pady = py)

def radBoton(tab, texto, variable, value, x, y, px, py):
    return ttk.Radiobutton(tab1, text = texto, variable = variable, value = 
    value).grid(row = x, column = y, padx = px, pady = py)

def cajita(texto, calificacion):
    mBox.showinfo("INFORMACION", texto+str(calificacion))

def cajita1(texto):
    mBox.showinfo("INFORMACION", texto)

def comando():
    check = 0
    primeras = 2
    check2 = 0
    check3 = 0
    dic = {}
    dic["pregunta1"] = entry_pregunta1.get()
    dic["pregunta2"] = entry_pregunta2.get()
    for k, v in dic.items():
        if not v:
            cajita1("TUS DATOS NO ESTAN COMPLETOS")
            break
    else:
        if(saldos_var.get() != 0 or tesoreria_var.get() != 0):
            check = 1 
        if (option == 1):
            check2 = 1
        if (option2 == 1):
            check3 = 1
        calificacion = primeras+check+check2+check3
        cajita('Tu calificaion es de: ', calificacion)

lab_pregunta1 = llenado1('tab1', "1.-¿Que son las finanzas?", 0, 0, 3, 3)
entry_pregunta1 = ttk.Entry(tab1, width = 50)
entry_pregunta1.grid(row =0, column = 1)


lab_pregunta2 = llenado1('tab1', "2.-¿Cual es el margen bruto?", 1, 0, 3, 3)
entry_pregunta2= ttk.Entry(tab1, width = 50)
entry_pregunta2.grid(row =1, column = 1)


lab_pregunta3 = llenado1('tab1', '3.-¿Cuanto le cuestan a tu empresa los retrasos?',2,0,3,3)

option = tk.IntVar()
rad1 = radBoton(tab1, '$10000', option, 1, 4, 0, 5, 5)
rad2 = radBoton(tab1, '$1800000', option, 2, 4, 1, 5, 5)
rad3 = radBoton(tab1, '$190000', option, 3, 4, 2, 5, 5)

lab_pegunta4 = llenado1('tab1', '4.-Cuanto es lo maximo que puede gastar tu empresa al año?',
5,0,3,3)

option2 = tk.IntVar()
rad4 = radBoton(tab1, '$10000000000', option2, 1, 6, 0, 5, 5)
rad5 = radBoton(tab1, '$20000000', option2, 2, 6, 1, 5, 5)
rad6 = radBoton(tab1, '$300000', option2, 3, 6, 2, 5, 5)


lab_pregunta5 = llenado1('tab1', '5.-Indica un ejemplo de un activo', 7,0,3,3)

tesoreria_var = tk.IntVar()
check1 = chBoton(tab1, 'tesoreria', tesoreria_var, 8, 0, 5, 5)

saldos_var = tk.IntVar()
check2 = chBoton(tab1, "Saldos", saldos_var, 8, 1, 5, 5)

mobiliario_var = tk.IntVar()
check3 = chBoton(tab1, "Mobiliario", mobiliario_var, 8, 3, 5, 5)

vehiculo_var = tk.IntVar()
check3 = chBoton(tab1, "Vehiculos", vehiculo_var, 8, 4, 5, 5)

oficina_var = tk.IntVar()
check3 = chBoton(tab1, "Oficina", oficina_var, 8, 5, 5, 5)

boton2 = defBoton('tab1', "Calificacion", 9, 3, comando)
main()

window.mainloop()