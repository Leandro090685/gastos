from datetime import datetime

def verificate_fecha(dato):
    try:
        datetime.strptime(dato,"%d/%m/%Y")
    except Exception:
        print ("Error al cargar la fecha")
        dato = input("Ingrese de nuevo la fecha: ")
        
        
def verificate_float(dato):
    """_summary_ Verify that the entered value is a float

    Returns:
        _type_: float: True
    """
    if dato == "":
        print ("Error el campo importe no puede estar vacio")
        dato = input("Ingrese el importe nuevamente: ")
    else:
        pass
    
    try:
        dato = float(dato)
        return True
    except Exception:
        print ("Error el campo importe debe ser numerico")
        dato = input("Ingrese el importe nuevamente: ")
        
def suma_imp(monto):
    total = 0
    for a in monto:
        total = total + a[0]
    return total
     