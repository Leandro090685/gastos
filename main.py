

from tkinter import END, INSERT, Menu, ttk
import tkinter as tk
from tkinter import Tk, Text
from tkinter import messagebox
from tkinter.ttk import Combobox
import pymysql
from models.gasto import Gasto
from models.rubro import Rubro
from servicies.service_gasto import ServiceGasto
from servicies.service_rubro import ServiceRubro
from datetime import datetime


def verificate_fecha():
    try:
        datetime.strptime(entry_fecha.get(),"%d/%m/%Y")
        return True
    except Exception:
        messagebox.showinfo(message="Dato Incorrecto en fecha", title="Error")
        

def registrar():
    """_summary_ checks entered values, creates the expense object and saves it in the database
    """
    
    if verificate_float(entry_importe.get()) and verificate_str() and verificate_fecha():
        a = Gasto(entry_fecha.get(),combo.get(),entry_descripcion.get(),entry_importe.get())
        ServiceGasto().save_gasto(a)
        clear()
        messagebox.showinfo(message="Gasto registrado con exito", title="Confirmacion")
    else: 
        pass
    
def verificate_str():
    """_summary_ Verify that the entered value is a string

    Returns:
        _type_: string: True
    """
    if entry_descripcion.get() == "":
        messagebox.showinfo(message="Campo descripcion vacio", title="Error")
        return False
    else:
        pass
    
    descripcion = entry_descripcion.get()
    try:
        descripcion = str(descripcion)
        return True
    except Exception:
        messagebox.showinfo(message="Dato Incorrecto en descripcion", title="Error")
        
def verificate_float(dato):
    """_summary_ Verify that the entered value is a float

    Returns:
        _type_: float: True
    """
    if dato == "":
        messagebox.showinfo(message="Campo Importe vacio", title="Error")
        return False
    else:
        pass
    
    try:
        dato = float(dato)
        return True
    except Exception:
        messagebox.showinfo(message="Dato Incorrecto en Importe", title="Error")
        return False
    
def clear():
    """_summary_ Delete the fields date, description and amount
    """
    entry_fecha.delete(0,END)
    entry_descripcion.delete(0,END)
    entry_importe.delete(0,END)
    

def ventana_rubro():
    """_summary_ Create the window to enter a new item
    """
    ventana_secundaria = tk.Toplevel()
    ventana_secundaria.title("Ingrese el nuevo rubro")
    ventana_secundaria.config(width=300, height=200)
    boton_confirmar = tk.Button(ventana_secundaria,text="Confirmar rubro",command=lambda:[confirmar(Rubro(entry_rubro.get())),entry_rubro.delete(0,END),ventana_secundaria.destroy()])
    boton_confirmar.place (x=100,y=100)
    entry_rubro = tk.Entry(ventana_secundaria)
    entry_rubro.place (x=90,y=50)


def confirmar(rubro:Rubro):
    ServiceRubro().save(rubro)
    lista_rubros = ServiceRubro().get_all()
    combo.configure(values=lista_rubros)
    messagebox.showinfo(message="Rubro creado con exito", title="Confirmacion")   

def delete_rubro():
    """_summary_ Create the window to enter a new item
    """
    lista_rubros = ServiceRubro().get_all() 
    ventana_terciaria = tk.Toplevel()
    ventana_terciaria.title("Rubro a eliminar")
    ventana_terciaria.config(width=300, height=200)
    boton_aceptar = tk.Button(ventana_terciaria,text="Aceptar",command=lambda:[borrar(combo.get()),ventana_terciaria.destroy()])
    boton_aceptar.place (x=100,y=100)
    combo = ttk.Combobox(ventana_terciaria, state="readonly",values= lista_rubros)
    combo.place (x=70,y=60)
    label_combo = tk.Label(text= "Rubro")
    label_combo.place (x=220,y=55)
    

def ventana_buscar():
    """_summary_ Create a new window to search by category
    """
    lista_rubros = ServiceRubro().get_all() 
    ventana_terciaria = tk.Toplevel()
    ventana_terciaria.title("Buscar gastos por rubro")
    ventana_terciaria.config(width=300, height=200)
    boton_aceptar = tk.Button(ventana_terciaria,text="Aceptar",command=lambda:buscar(combo.get()))
    boton_aceptar.place (x=100,y=100)
    combo = ttk.Combobox(ventana_terciaria, state="readonly",values= lista_rubros)
    combo.place (x=70,y=60)
    label_combo = tk.Label(text= "Rubro")
    label_combo.place (x=220,y=55)
    
    
           
def borrar(rubro:str):
    ServiceRubro().clear_rubro(rubro)
    lista_rubros = ServiceRubro().get_all()
    combo.configure(values=lista_rubros)
    messagebox.showinfo(message="Rubro eliminado", title="Confirmacion")
           

    
def buscar(rubro):
    tabla = ServiceGasto().get_one(rubro)
    ventana_tabla= tk.Tk()
    ventana_tabla.geometry("500x200")
    ventana_tabla.resizable(False, False)
    ventana_tabla.title("Gastos por rubro")
    total = suma(ServiceGasto().total_rubro(rubro))
    label_total = tk.Label(ventana_tabla,text=f"Gasto total ${total}")
    label_total.place (x=10, y=180)
    text = Text(ventana_tabla, height=10)
    text.pack()
    text.insert('1.0', tabla)
    ventana_tabla.mainloop()
    
def ver():
    """_summary_ Shows all the expenses registered in the database through a table
    """
    tabla_total=ServiceGasto().get_all_table()
    ventana_tabla_total= tk.Tk()
    ventana_tabla_total.geometry("500x200")
    ventana_tabla_total.resizable(False, False)
    ventana_tabla_total.title("Gastos")
    total = suma(ServiceGasto().total())
    label_total = tk.Label(ventana_tabla_total,text=f"Gasto total ${total}")
    label_total.place (x=10, y=180)
    text = Text(ventana_tabla_total, height=10)
    text.insert(INSERT,tabla_total)
    text.pack()
    ventana_tabla_total.mainloop()
    
def temp_text(e):
   entry_fecha.delete(0,"end")
   
def suma(monto):
    total = 0
    for a in monto:
        total = total + a[0]
    return total

def ventana_borrar_gasto():
    tabla_total=ServiceGasto().get_all_table()
    ventana_tabla_total= tk.Tk()
    ventana_tabla_total.geometry("500x200")
    ventana_tabla_total.resizable(False, False)
    ventana_tabla_total.title("Gastos")
    text = Text(ventana_tabla_total, height=10)
    text.insert(INSERT,tabla_total)
    text.pack() 
    label_id_borrar = tk.Label(ventana_tabla_total,text="Ingrese el ID del gasto a eliminar")
    label_id_borrar.place (x=10, y=180)
    id_borrar = tk.Entry(ventana_tabla_total)
    id_borrar.place (x=200, y=180)
    btn_aceptar = tk.Button(ventana_tabla_total, text="Aceptar",command=lambda:[borrar_gasto(id_borrar.get()),ventana_tabla_total.destroy()])
    btn_aceptar.place (x=350,y=175)
    ventana_tabla_total.mainloop()

def borrar_gasto(id):
    try:
        id = int(id)
    except Exception:
        messagebox.showinfo(message="Id incorrecto", title="Error")
        return False
    if messagebox.askyesno (message="¿Desea borrar el gasto con el id "f"{id}""?", title="Confirmacion"):
        ServiceGasto().clear_gasto(id)
    else:
        pass
      
    
    
   
lista_rubros = ServiceRubro().get_all() 
 
 
if __name__ == "__main__":   


    window = tk.Tk()
    window.title("Gastos")
    window.config(width=500, height=400)

    barra_menu = tk.Menu()
    window.config(menu=barra_menu)
    menu_archivo = tk.Menu(barra_menu, tearoff=False)
    menu_ver = tk.Menu(barra_menu,tearoff=False)
    barra_menu.add_cascade(menu = menu_archivo, label="Rubro")
    barra_menu.add_cascade(menu=menu_ver,label="Ver")
    menu_archivo.add_command(label="Nuevo rubro",command=ventana_rubro)
    menu_archivo.add_command(label="Eliminar rubro",command=delete_rubro)
    menu_ver.add_command(label="Todos los gastos",command=ver)
    menu_ver.add_command(label="Buscar gastos por rubro",command=ventana_buscar)
    menu_ver.add_command(label="Borrar gasto",command=ventana_borrar_gasto)


    label_fecha = tk.Label(text= "Fecha")
    label_fecha.place (x=60, y=60)
    entry_fecha = tk.Entry()
    entry_fecha.insert(0, "dd/mm/yyyy")
    entry_fecha.bind("<FocusIn>", temp_text)
    entry_fecha.place (x=20, y=80)

    label_importe = tk.Label(text= "Importe")
    label_importe.place (x=390, y=60)
    entry_importe = tk.Entry()
    entry_importe.place (x=350, y=80)

    label_descripcion = tk.Label(text= "Descripcion")
    label_descripcion.place (x=180, y=160)
    entry_descripcion = tk.Entry()
    entry_descripcion.place (x=20, y=180,width=400)

    combo = ttk.Combobox(
        state="readonly",
        values= lista_rubros)
    combo.pack()
    combo.place (x=170,y=80)
    label_combo = tk.Label(text= "Rubro")
    label_combo.place (x=220,y=55)
    
    btn_registrar_gasto = tk.Button(text="Registrar gasto",command=registrar)
    btn_registrar_gasto.place (x=360,y=220)
    

    window.mainloop()
    