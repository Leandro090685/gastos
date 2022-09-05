from models.gasto import Gasto
from models.rubro import Rubro
from servicies.service_rubro import ServiceRubro
from servicies.funciones import *
from datetime import datetime
from servicies.service_gasto import ServiceGasto
import time

while True:
    print (
            """Menu:
            1) Registrar un gasto
            2) Ver todos los gastos
            3) Ver gastos por rubro
            4) Borrar un gasto
            5) Nuevo rubro
            6) Eliminar rubro
            """)
    opcion = input("Ingrese la opcion deseada: ")
    if opcion == "1":
        fecha = input("Ingrese la fecha del gasto en formato dd/mm/yyyy: ")
        verificate_fecha(fecha)
        print ("------------------------------------")
        for n in (ServiceRubro().get_all()):
            for i in n:
                print (i)
        print ("------------------------------------")
        rubro= input("Escoga un rubro de la siguiente lista: ")
        if rubro not in n:
            print ("Ese rubro no existe")
            rubro = input("Escoga un rubro correcto: ")
        else:
            pass
        descripcion = input("Ingrese una descripcion: ")
        importe = input("Ingrese el importe del gasto en pesos: ")
        verificate_float(importe)
        a = Gasto(fecha,rubro,descripcion,importe)
        ServiceGasto().save_gasto(a)
        print ("------------------------------------")
        print ("Gasto guardado con exito")
        print ("------------------------------------")
        time.sleep(3)
    if opcion == "2":
        tabla = ServiceGasto().get_all_table()
        print (tabla)
        total = suma_imp(ServiceGasto().total())
        print (f"Total: ${total}")
        #print (f"Total={total}")
        time.sleep(5)
    if opcion == "3":
        print ("------------------------------------")
        for n in (ServiceRubro().get_all()):
            for i in n:
                print (i)
        print ("------------------------------------")
        rubro = input("Escoga el rubro del cual quiere ver los gastos: ")
        gasto_uno = ServiceGasto().get_one(rubro)
        print (gasto_uno)
        total = suma_imp(ServiceGasto().total_rubro(rubro))
        print (f"Total: ${total}")
        time.sleep(5)
    if opcion == "4":
        tabla = ServiceGasto().get_all_table()
        print ("------------------------------------")
        print (tabla)
        print ("------------------------------------")
        id = input("Ingrese el id del gasto que desea borrar: ")
        ServiceGasto().clear_gasto(id)
        print ("Gasto borrado con exito")
        tabla = ServiceGasto().get_all_table()
        print (tabla)
        time.sleep(5)
    if opcion == "5":
        rubro = input("Ingrese el nombre del rubro nuevo: ")
        a = Rubro(rubro)
        ServiceRubro().save(a)
        print("Rubro agregado con exito")
        for n in (ServiceRubro().get_all()):
            for i in n:
                print (i)
        time.sleep(5)
    if opcion == "6":
        print ("------------------------------------")
        for n in (ServiceRubro().get_all()):
            for i in n:
                print (i)
        print ("------------------------------------")
        rubro = input("Ingrese el nombre del rubro que desea eliminar: ")
        ServiceRubro().clear_rubro(rubro)
        print("Rubro eliminado con exito")
        time.sleep(5)
        print ("------------------------------------")
        for n in (ServiceRubro().get_all()):
            for i in n:
                print (i)
        print ("------------------------------------")
        time.sleep(5)
        
        
        
        
        